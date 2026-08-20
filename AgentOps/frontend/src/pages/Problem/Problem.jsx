import { useEffect, useMemo, useRef, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import Editor from '@monaco-editor/react'

import {
  ArrowLeft,
  CheckCircle2,
  Lightbulb,
  Play,
  RotateCcw,
  Send,
  Sparkles,
  XCircle,
  Loader2
} from 'lucide-react'

import { problems } from '../../data/problem'


function Problem() {
  const { id } = useParams()

  const navigate = useNavigate()


  // --------------------------------------------------
  // Find problem
  // --------------------------------------------------

  const problem = useMemo(() => {
    return problems.find(
      (item) => String(item.id) === String(id)
    )
  }, [id])


  // --------------------------------------------------
  // State
  // --------------------------------------------------

  const [language, setLanguage] = useState('java')

  const [code, setCode] = useState(
    problem?.starterCode?.java || ''
  )

  const [codeByLanguage, setCodeByLanguage] = useState({
    java: problem?.starterCode?.java || '',
    python: problem?.starterCode?.python || '',
    javascript: problem?.starterCode?.javascript || ''
  })

  /*
    executionResult:

    null

    OR

    {
      type: 'run' | 'submit',
      status: 'running' | 'passed' | 'failed',
      message: string,
      runtime: string,
      memory: string
    }
  */

  const [executionResult, setExecutionResult] = useState(null)

  // idle → running → passed / failed
  const [runStatus, setRunStatus] = useState('idle')

  // idle → submitting → passed / failed
  const [submitStatus, setSubmitStatus] = useState('idle')

  const [activeTab, setActiveTab] = useState('testcases')

  const [showHint, setShowHint] = useState(false)

  const [hintIndex, setHintIndex] = useState(0)

  // Used to clean up simulated execution timers
  const executionTimerRef = useRef(null)


  // --------------------------------------------------
  // Language templates
  // --------------------------------------------------

  const languageTemplates = useMemo(() => {
    if (!problem) {
      return {
        java: '',
        python: '',
        javascript: ''
      }
    }

    return {
      java: problem.starterCode?.java || '',
      python: problem.starterCode?.python || '',
      javascript: problem.starterCode?.javascript || ''
    }
  }, [problem])


  // --------------------------------------------------
  // Cleanup execution timer
  // --------------------------------------------------

  useEffect(() => {
    return () => {
      if (executionTimerRef.current) {
        clearTimeout(executionTimerRef.current)
      }
    }
  }, [])


  // --------------------------------------------------
  // Reset everything when problem changes
  // --------------------------------------------------

  useEffect(() => {
    if (!problem) {
      setCode('')

      setCodeByLanguage({
        java: '',
        python: '',
        javascript: ''
      })

      setExecutionResult(null)

      setRunStatus('idle')

      setSubmitStatus('idle')

      setActiveTab('testcases')

      setShowHint(false)

      setHintIndex(0)

      return
    }

    const newCodeByLanguage = {
      java: problem.starterCode?.java || '',
      python: problem.starterCode?.python || '',
      javascript: problem.starterCode?.javascript || ''
    }

    setLanguage('java')

    setCodeByLanguage(newCodeByLanguage)

    setCode(newCodeByLanguage.java)

    setExecutionResult(null)

    setRunStatus('idle')

    setSubmitStatus('idle')

    setActiveTab('testcases')

    setShowHint(false)

    setHintIndex(0)

  }, [problem])


  // --------------------------------------------------
  // Helper: clear execution state
  // --------------------------------------------------

  const clearExecutionState = () => {
    setExecutionResult(null)

    setRunStatus('idle')

    setSubmitStatus('idle')
  }


  // --------------------------------------------------
  // Run code
  // --------------------------------------------------

  const handleRun = () => {

    // Prevent duplicate execution
    if (
      runStatus === 'running' ||
      submitStatus === 'submitting'
    ) {
      return
    }


    // Basic empty-code validation
    if (!code.trim()) {

      setExecutionResult({
        type: 'run',
        status: 'failed',
        message: 'Your code is empty. Write a solution before running it.',
        runtime: '-',
        memory: '-'
      })

      setRunStatus('failed')

      setSubmitStatus('idle')

      setActiveTab('output')

      return
    }


    // Running state
    setRunStatus('running')

    setSubmitStatus('idle')


    // Open output automatically
    setActiveTab('output')


    // Show running result
    setExecutionResult({
      type: 'run',
      status: 'running',
      message: 'Running test cases...',
      runtime: '-',
      memory: '-'
    })


    // Clear previous timer
    if (executionTimerRef.current) {
      clearTimeout(executionTimerRef.current)
    }


    // --------------------------------------------------
    // Temporary simulation
    //
    // Later this will become:
    //
    // API → backend → compiler → test cases
    // --------------------------------------------------

    executionTimerRef.current = setTimeout(() => {

      setRunStatus('passed')

      setExecutionResult({
        type: 'run',
        status: 'passed',
        message: 'Test case 1 passed successfully.',
        runtime: '2 ms',
        memory: '42 MB'
      })

    }, 800)
  }


  // --------------------------------------------------
  // Submit
  // --------------------------------------------------

  const handleSubmit = () => {

    // Prevent duplicate execution
    if (
      runStatus === 'running' ||
      submitStatus === 'submitting'
    ) {
      return
    }


    // Basic empty-code validation
    if (!code.trim()) {

      setExecutionResult({
        type: 'submit',
        status: 'failed',
        message: 'Your code is empty. Write a solution before submitting it.',
        runtime: '-',
        memory: '-'
      })

      setSubmitStatus('failed')

      setRunStatus('idle')

      setActiveTab('output')

      return
    }


    // Submitting state
    setSubmitStatus('submitting')

    setRunStatus('idle')


    // Open output
    setActiveTab('output')


    // Show submitting state
    setExecutionResult({
      type: 'submit',
      status: 'running',
      message: 'Submitting solution...',
      runtime: '-',
      memory: '-'
    })


    // Clear previous timer
    if (executionTimerRef.current) {
      clearTimeout(executionTimerRef.current)
    }


    // --------------------------------------------------
    // Temporary simulation
    //
    // Later this will connect to backend execution.
    // --------------------------------------------------

    executionTimerRef.current = setTimeout(() => {

      setSubmitStatus('passed')

      setExecutionResult({
        type: 'submit',
        status: 'passed',
        message: 'All test cases passed successfully.',
        runtime: '2 ms',
        memory: '42 MB'
      })

    }, 1000)
  }


  // --------------------------------------------------
  // Reset code
  // --------------------------------------------------

  const handleReset = () => {

    const starterCode =
      languageTemplates[language] || ''


    setCode(starterCode)


    setCodeByLanguage((prev) => ({
      ...prev,
      [language]: starterCode
    }))


    clearExecutionState()


    setActiveTab('testcases')

    setShowHint(false)

    setHintIndex(0)
  }


  // --------------------------------------------------
  // Change language
  // --------------------------------------------------

  const handleLanguageChange = (newLanguage) => {

    setLanguage(newLanguage)


    setCode(
      codeByLanguage[newLanguage] ||
      languageTemplates[newLanguage] ||
      ''
    )


    clearExecutionState()


    setActiveTab('testcases')
  }


  // --------------------------------------------------
  // Monaco before mount
  // --------------------------------------------------

  const handleEditorWillMount = (monaco) => {
    // Monaco is available here before the editor mounts.
    // We intentionally don't modify Monaco internals.
  }


  // --------------------------------------------------
  // Monaco mounted
  // --------------------------------------------------

  const handleEditorMount = (editor) => {
    editor.focus()
  }


  // --------------------------------------------------
  // Monaco error
  // --------------------------------------------------

  const handleEditorError = (error) => {
    console.error('Monaco Editor Error:', error)
  }


  // --------------------------------------------------
  // Problem not found
  // --------------------------------------------------

  if (!problem) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">

        <div className="text-center">

          <h1 className="text-xl font-semibold text-slate-900">
            Problem not found
          </h1>

          <Link
            to="/practice"
            className="inline-flex items-center gap-2 mt-4 text-sm text-blue-600 hover:text-blue-700"
          >
            <ArrowLeft size={16} />

            Back to Practice
          </Link>

        </div>

      </div>
    )
  }


  // --------------------------------------------------
  // Derived execution values
  // --------------------------------------------------

  const isRunning =
    runStatus === 'running'

  const isSubmitting =
    submitStatus === 'submitting'

  const isExecuting =
    isRunning || isSubmitting


  const resultStatus =
    executionResult?.status


  return (
    <div className="max-w-[1500px] mx-auto pb-8">


      {/* =====================================================
          BACK
      ====================================================== */}

      <Link
        to="/practice"
        className="inline-flex items-center gap-2 mb-4 text-xs font-medium text-slate-500 hover:text-slate-900 transition"
      >
        <ArrowLeft size={14} />

        Back to Practice
      </Link>


      {/* =====================================================
          PROBLEM HEADER
      ====================================================== */}

      <div className="bg-white border border-slate-200 rounded-2xl px-6 py-5 mb-4 shadow-sm">

        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

          <div>

            <div className="flex flex-wrap items-center gap-3">

              <h1 className="text-xl font-bold tracking-tight text-slate-900">
                {problem.title}
              </h1>

              <span className="px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 text-[11px] font-semibold">
                {problem.difficulty}
              </span>

            </div>


            <div className="flex items-center gap-2 mt-1.5 text-xs text-slate-500">

              <span>
                {problem.topic}
              </span>

              <span className="text-slate-300">
                •
              </span>

              <span>
                {problem.pattern}
              </span>

            </div>

          </div>


          <div className="flex items-center gap-2">

            <button
              type="button"
              onClick={() => {
                setShowHint((prev) => !prev)
                setHintIndex(0)
              }}
              className="inline-flex items-center gap-2 px-3.5 py-2 rounded-lg border border-slate-200 bg-white text-xs font-semibold text-slate-600 hover:bg-slate-50 hover:border-slate-300 transition"
            >
              <Lightbulb size={15} />

              {showHint ? 'Hide Hint' : 'Hint'}
            </button>


            <button
              type="button"
              onClick={() => {
                navigate('/ai-coach', {
                  state: {
                    problem,
                    code,
                    language
                  }
                })
              }}
              className="inline-flex items-center gap-2 px-3.5 py-2 rounded-lg bg-slate-900 text-white text-xs font-semibold hover:bg-slate-800 transition shadow-sm"
            >
              <Sparkles size={15} />

              AI Coach
            </button>

          </div>

        </div>

      </div>


      {/* =====================================================
          MAIN WORKSPACE
      ====================================================== */}

      <div className="grid grid-cols-1 xl:grid-cols-[0.92fr_1.08fr] gap-4">


        {/* ===================================================
            LEFT SIDE
        ==================================================== */}

        <section className="h-[700px] bg-white border border-slate-200 rounded-2xl shadow-sm flex flex-col overflow-hidden">

          <div className="px-6 pt-5">

            <div className="flex items-center gap-2">

              <div className="w-7 h-7 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center">

                <span className="text-xs font-bold">
                  ?
                </span>

              </div>

              <h2 className="text-sm font-semibold text-slate-900">
                Problem
              </h2>

            </div>

          </div>


          <div className="flex-1 overflow-y-auto px-6 pt-4 pb-5">

            <p className="text-sm leading-6 text-slate-600">
              {problem.description}
            </p>


            {/* ------------------------------------------------
                Examples
            ------------------------------------------------- */}

            <div className="mt-6">

              <h3 className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                Example
              </h3>


              {problem.examples?.map((example, index) => (

                <div
                  key={index}
                  className="mt-3 rounded-xl bg-slate-950 border border-slate-800 p-4 font-mono text-xs leading-6 shadow-sm"
                >

                  <div>

                    <span className="text-slate-500">
                      Input
                    </span>

                    <p className="mt-1 text-slate-300 break-words">
                      {example.input}
                    </p>

                  </div>


                  <div className="mt-4">

                    <span className="text-slate-500">
                      Output
                    </span>

                    <p className="mt-1 text-slate-300 break-words">
                      {example.output}
                    </p>

                  </div>

                </div>

              ))}

            </div>


            {/* ------------------------------------------------
                Constraints
            ------------------------------------------------- */}

            <div className="mt-6">

              <h3 className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                Constraints
              </h3>


              <ul className="mt-3 space-y-2">

                {problem.constraints?.map((constraint, index) => (

                  <li
                    key={index}
                    className="flex items-start gap-2 text-xs leading-5 text-slate-600"
                  >

                    <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-slate-300 shrink-0" />

                    <span>
                      {constraint}
                    </span>

                  </li>

                ))}

              </ul>

            </div>


            {/* ------------------------------------------------
                Hint
            ------------------------------------------------- */}

            {showHint && (

              <div className="mt-6 rounded-xl border border-amber-200 bg-amber-50 p-4">

                <div className="flex items-start gap-3">

                  <div className="w-7 h-7 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center shrink-0">

                    <Lightbulb size={15} />

                  </div>


                  <div className="min-w-0">

                    <p className="text-xs font-semibold text-amber-900">
                      Hint {hintIndex + 1}
                    </p>


                    <p className="mt-1 text-xs leading-5 text-amber-800">
                      {problem.hints?.[hintIndex] ||
                        'No hint available.'}
                    </p>


                    {problem.hints &&
                      hintIndex < problem.hints.length - 1 && (

                        <button
                          type="button"
                          onClick={() =>
                            setHintIndex((prev) => prev + 1)
                          }
                          className="mt-3 text-xs font-semibold text-amber-700 hover:text-amber-900"
                        >
                          Show next hint →
                        </button>

                      )}

                  </div>

                </div>

              </div>

            )}

          </div>


          {/* =================================================
              AI COACH
          ================================================== */}

          <div className="border-t border-slate-100 px-6 py-4 bg-slate-50/70">

            <div className="flex items-start gap-3">

              <div className="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center shrink-0 shadow-sm">

                <Sparkles size={15} />

              </div>


              <div>

                <p className="text-xs font-semibold text-slate-900">
                  Need help?
                </p>

                <p className="mt-0.5 text-[11px] leading-4 text-slate-500">
                  Get guidance without immediately revealing the solution.
                </p>

              </div>

            </div>


            <div className="flex flex-wrap gap-2 mt-3">

              <button
                type="button"
                onClick={() => {
                  setShowHint(true)
                  setHintIndex(0)
                }}
                className="px-2.5 py-1.5 rounded-lg border border-slate-200 bg-white text-[11px] font-medium text-slate-600 hover:border-blue-200 hover:text-blue-600 transition"
              >
                Give me a hint
              </button>


              <button
                type="button"
                className="px-2.5 py-1.5 rounded-lg border border-slate-200 bg-white text-[11px] font-medium text-slate-600 hover:border-blue-200 hover:text-blue-600 transition"
              >
                Explain approach
              </button>


              <button
                type="button"
                className="px-2.5 py-1.5 rounded-lg border border-slate-200 bg-white text-[11px] font-medium text-slate-600 hover:border-blue-200 hover:text-blue-600 transition"
              >
                Analyze mistake
              </button>

            </div>

          </div>

        </section>


        {/* ===================================================
            RIGHT CODE WORKSPACE
        ==================================================== */}

        <section className="h-[700px] rounded-2xl bg-slate-950 border border-slate-800 shadow-lg overflow-hidden flex flex-col">


          {/* ------------------------------------------------
              Editor header
          ------------------------------------------------- */}

          <div className="h-12 shrink-0 px-5 flex items-center justify-between border-b border-slate-800 bg-slate-950">

            <div className="flex items-center gap-3">

              {/* Execution indicator */}

              <div
                className={`w-2 h-2 rounded-full transition ${
                  isExecuting
                    ? 'bg-blue-400 animate-pulse'
                    : resultStatus === 'passed'
                      ? 'bg-emerald-400'
                      : resultStatus === 'failed'
                        ? 'bg-red-400'
                        : 'bg-blue-500'
                }`}
              />


              {/* Language */}

              <select
                value={language}
                onChange={(e) =>
                  handleLanguageChange(e.target.value)
                }
                disabled={isExecuting}
                className="bg-slate-900 border border-slate-800 rounded-lg px-3 py-1.5 text-xs font-semibold text-slate-300 outline-none cursor-pointer focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >

                <option value="java">
                  Java
                </option>

                <option value="python">
                  Python
                </option>

                <option value="javascript">
                  JavaScript
                </option>

              </select>


              {/* Status label */}

              {isRunning && (
                <span className="text-[10px] font-medium text-blue-400">
                  Running
                </span>
              )}

              {isSubmitting && (
                <span className="text-[10px] font-medium text-blue-400">
                  Submitting
                </span>
              )}

              {!isExecuting &&
                resultStatus === 'passed' && (
                  <span className="text-[10px] font-medium text-emerald-400">
                    Passed
                  </span>
                )}

              {!isExecuting &&
                resultStatus === 'failed' && (
                  <span className="text-[10px] font-medium text-red-400">
                    Failed
                  </span>
                )}

            </div>


            {/* Reset */}

            <button
              type="button"
              onClick={handleReset}
              disabled={isExecuting}
              className="p-1.5 rounded-md text-slate-500 hover:text-slate-200 hover:bg-slate-900 disabled:opacity-40 disabled:cursor-not-allowed transition"
              title="Reset code"
            >
              <RotateCcw size={15} />
            </button>

          </div>


          {/* =================================================
              MONACO EDITOR
          ================================================== */}

          <div className="flex-1 min-h-0 overflow-hidden bg-[#020617]">

            <Editor
              height="100%"
              language={language}
              value={code}
              theme="vs-dark"

              onChange={(value) => {

                const newCode = value || ''

                setCode(newCode)

                setCodeByLanguage((prev) => ({
                  ...prev,
                  [language]: newCode
                }))


                /*
                  If the user edits the code after a result,
                  return the execution UI to idle.
                */

                if (!isExecuting) {
                  setExecutionResult(null)

                  setRunStatus('idle')

                  setSubmitStatus('idle')
                }

              }}

              options={{
                minimap: {
                  enabled: false
                },

                automaticLayout: true
              }}
            />

          </div>


          {/* =================================================
              ACTIONS
          ================================================== */}

          <div className="h-14 shrink-0 px-5 border-t border-slate-800 flex items-center justify-between bg-slate-950">


            {/* RUN */}

            <button
              type="button"
              onClick={handleRun}
              disabled={isExecuting}

              className="inline-flex items-center gap-2 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-900 disabled:opacity-40 disabled:cursor-not-allowed transition"
            >

              {isRunning ? (
                <Loader2
                  size={14}
                  className="animate-spin"
                />
              ) : (
                <Play size={14} />
              )}

              {isRunning
                ? 'Running...'
                : 'Run'}

            </button>


            {/* SUBMIT */}

            <button
              type="button"
              onClick={handleSubmit}
              disabled={isExecuting}

              className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-blue-600 text-white text-xs font-semibold hover:bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition shadow-sm"
            >

              {isSubmitting ? (
                <Loader2
                  size={14}
                  className="animate-spin"
                />
              ) : (
                <Send size={14} />
              )}

              {isSubmitting
                ? 'Submitting...'
                : 'Submit'}

            </button>

          </div>


          {/* =================================================
              TEST CASE / OUTPUT
          ================================================== */}

          <div className="h-[185px] shrink-0 border-t border-slate-800 bg-slate-950">


            {/* ------------------------------------------------
                Tabs
            ------------------------------------------------- */}

            <div className="h-10 px-5 flex items-center gap-5 border-b border-slate-800">

              <button
                type="button"
                onClick={() =>
                  setActiveTab('testcases')
                }

                className={`h-full text-[11px] font-semibold border-b-2 transition ${
                  activeTab === 'testcases'
                    ? 'text-white border-blue-500'
                    : 'text-slate-500 border-transparent hover:text-slate-300'
                }`}
              >
                Test Cases
              </button>


              <button
                type="button"
                onClick={() =>
                  setActiveTab('output')
                }

                className={`h-full text-[11px] font-semibold border-b-2 transition ${
                  activeTab === 'output'
                    ? 'text-white border-blue-500'
                    : 'text-slate-500 border-transparent hover:text-slate-300'
                }`}
              >
                Output

                {executionResult && (
                  <span
                    className={`ml-2 inline-block w-1.5 h-1.5 rounded-full ${
                      executionResult.status === 'running'
                        ? 'bg-blue-400 animate-pulse'
                        : executionResult.status === 'passed'
                          ? 'bg-emerald-400'
                          : 'bg-red-400'
                    }`}
                  />
                )}

              </button>

            </div>


            {/* ------------------------------------------------
                Test Cases
            ------------------------------------------------- */}

            {activeTab === 'testcases' && (

              <div className="h-[145px] overflow-y-auto p-4 space-y-2">

                {problem.testCases?.length > 0 ? (

                  problem.testCases.map((testCase, index) => (

                    <div
                      key={index}
                      className="rounded-lg border border-slate-800 bg-slate-900/70 p-3"
                    >

                      <div className="flex items-center justify-between">

                        <span className="text-[10px] font-semibold text-slate-500 uppercase tracking-wider">
                          Test Case {index + 1}
                        </span>

                        {executionResult?.status === 'passed' && (
                          <CheckCircle2
                            size={13}
                            className="text-emerald-400"
                          />
                        )}

                      </div>


                      <p className="mt-2 text-xs font-mono text-slate-300 break-words">
                        {testCase.input || 'No input available.'}
                      </p>


                      <div className="mt-2 flex items-center gap-2">

                        <span className="text-[10px] text-slate-500">
                          Expected:
                        </span>

                        <span className="text-xs font-mono text-slate-300">
                          {testCase.expected || '-'}
                        </span>

                      </div>

                    </div>

                  ))

                ) : (

                  <div className="h-full flex items-center justify-center text-xs text-slate-600">
                    No test cases available.
                  </div>

                )}

              </div>

            )}


            {/* ------------------------------------------------
                Output
            ------------------------------------------------- */}

            {activeTab === 'output' && (

              <div className="h-[145px] overflow-y-auto p-4">

                {!executionResult ? (

                  <div className="h-full flex flex-col items-center justify-center">

                    <div className="w-8 h-8 rounded-lg bg-slate-900 flex items-center justify-center mb-2">

                      <Play
                        size={14}
                        className="text-slate-600"
                      />

                    </div>

                    <p className="text-xs text-slate-600">
                      Run your code to see the output.
                    </p>

                  </div>

                ) : (

                  <div
                    className={`rounded-xl border p-3 transition ${
                      executionResult.status === 'running'
                        ? 'border-blue-900/40 bg-blue-950/20'
                        : executionResult.status === 'passed'
                          ? 'border-emerald-900/40 bg-emerald-950/20'
                          : 'border-red-900/40 bg-red-950/20'
                    }`}
                  >

                    {/* Result header */}

                    <div className="flex items-center justify-between">

                      <div className="flex items-center gap-2">

                        {executionResult.status === 'running' && (

                          <Loader2
                            size={14}
                            className="text-blue-400 animate-spin"
                          />

                        )}


                        {executionResult.status === 'passed' && (

                          <CheckCircle2
                            size={14}
                            className="text-emerald-400"
                          />

                        )}


                        {executionResult.status === 'failed' && (

                          <XCircle
                            size={14}
                            className="text-red-400"
                          />

                        )}


                        <span
                          className={`text-xs font-semibold ${
                            executionResult.status === 'running'
                              ? 'text-blue-300'
                              : executionResult.status === 'passed'
                                ? 'text-emerald-300'
                                : 'text-red-300'
                          }`}
                        >

                          {executionResult.status === 'running'
                            ? executionResult.type === 'run'
                              ? 'Running'
                              : 'Submitting'
                            : executionResult.status === 'passed'
                              ? executionResult.type === 'run'
                                ? 'Execution Passed'
                                : 'Submission Accepted'
                              : 'Execution Failed'}

                        </span>

                      </div>


                      {/* Type badge */}

                      <span className="text-[9px] uppercase tracking-wider font-semibold text-slate-500">

                        {executionResult.type}

                      </span>

                    </div>


                    {/* Result message */}

                    <p className="mt-3 text-xs leading-5 text-slate-300">
                      {executionResult.message}
                    </p>


                    {/* Runtime information */}

                    {executionResult.status === 'passed' && (

                      <div className="mt-3 flex items-center gap-4">

                        <div>

                          <p className="text-[9px] uppercase tracking-wider text-slate-600">
                            Runtime
                          </p>

                          <p className="mt-0.5 text-[11px] font-mono text-slate-400">
                            {executionResult.runtime}
                          </p>

                        </div>


                        <div>

                          <p className="text-[9px] uppercase tracking-wider text-slate-600">
                            Memory
                          </p>

                          <p className="mt-0.5 text-[11px] font-mono text-slate-400">
                            {executionResult.memory}
                          </p>

                        </div>

                      </div>

                    )}

                  </div>

                )}

              </div>

            )}

          </div>

        </section>

      </div>

    </div>
  )
}


export default Problem