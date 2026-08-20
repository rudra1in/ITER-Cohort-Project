import { useEffect, useMemo, useRef, useState } from 'react'

import {
  Bot,
  Brain,
  Check,
  ChevronDown,
  Code2,
  Lightbulb,
  MessageCircle,
  RefreshCcw,
  Send,
  Sparkles,
  X,
  Search,
  FileCode2
} from 'lucide-react'

import ReactMarkdown from 'react-markdown'
import remarkMath from 'remark-math'
import rehypeKatex from 'rehype-katex'
import 'katex/dist/katex.min.css'

import { useLocation } from 'react-router-dom'

import { getCoachResponse } from '../../services/aiCoachService'


// ============================================================
// COACHING MODES
// ============================================================

const coachingModes = [
  {
    id: 'hint',
    label: 'Give me a hint',
    description: 'Get guidance without seeing the solution.',
    icon: Lightbulb
  },
  {
    id: 'explain',
    label: 'Explain approach',
    description: 'Understand the problem-solving strategy.',
    icon: Brain
  },
  {
    id: 'analyze',
    label: 'Analyze mistake',
    description: 'Find where your reasoning went wrong.',
    icon: Search
  },
  {
    id: 'review',
    label: 'Review my code',
    description: 'Get feedback on your current solution.',
    icon: Code2
  }
]


// ============================================================
// QUICK PROMPTS
// ============================================================

const quickPrompts = [
  'Give me a hint',
  'Explain the approach',
  'What should I think about first?',
  'What is the time complexity?'
]


// ============================================================
// MESSAGE CONTENT
// ============================================================
//
// ReactMarkdown handles:
// - **bold**
// - *italic*
// - `inline code`
// - ```code blocks```
// - headings
// - lists
// - links
// - LaTeX math using remark-math + rehype-katex
//
// Example:
// $$O(\log N)$$
// will be rendered as mathematical notation instead of showing
// the dollar signs.
//

function renderMessageContent(content) {

  if (content === null || content === undefined) {
    return null
  }


  // ----------------------------------------------------------
  // Make sure content is always a string
  // ----------------------------------------------------------

  if (typeof content !== 'string') {

    if (typeof content === 'object') {

      content =
        content.answer ||
        content.response ||
        content.content ||
        JSON.stringify(content, null, 2)

    } else {

      content = String(content)

    }

  }


  return (
    <ReactMarkdown
      remarkPlugins={[remarkMath]}
      rehypePlugins={[rehypeKatex]}

      components={{

        // ----------------------------------------------------
        // Paragraph
        // ----------------------------------------------------

        p: ({ children }) => (
          <p className="mb-3 last:mb-0 text-slate-700">
            {children}
          </p>
        ),


        // ----------------------------------------------------
        // Headings
        // ----------------------------------------------------

        h1: ({ children }) => (
          <h1 className="text-base font-bold text-slate-900 mb-3 mt-4 first:mt-0">
            {children}
          </h1>
        ),

        h2: ({ children }) => (
          <h2 className="text-sm font-bold text-slate-900 mb-2 mt-4 first:mt-0">
            {children}
          </h2>
        ),

        h3: ({ children }) => (
          <h3 className="text-sm font-semibold text-slate-900 mb-2 mt-3 first:mt-0">
            {children}
          </h3>
        ),


        // ----------------------------------------------------
        // Strong / Bold
        // ----------------------------------------------------

        strong: ({ children }) => (
          <strong className="font-semibold text-slate-900">
            {children}
          </strong>
        ),

        em: ({ children }) => (
          <em className="italic text-slate-700">
            {children}
          </em>
        ),


        // ----------------------------------------------------
        // Lists
        // ----------------------------------------------------

        ul: ({ children }) => (
          <ul className="list-disc pl-5 mb-3 space-y-1 text-slate-700">
            {children}
          </ul>
        ),

        ol: ({ children }) => (
          <ol className="list-decimal pl-5 mb-3 space-y-1 text-slate-700">
            {children}
          </ol>
        ),

        li: ({ children }) => (
          <li className="leading-6 text-slate-700">
            {children}
          </li>
        ),


        // ----------------------------------------------------
        // Inline Code
        // ----------------------------------------------------

        code: ({className, children, ...props }) => {

          const isCodeBlock =
          Boolean(className?.startsWith('language-')) ||
          String(children).includes('\n')

          if (!isCodeBlock) {

            return (
              <code
                className="px-1.5 py-0.5 rounded bg-slate-200 text-slate-900 font-mono text-[11px] font-medium"
                {...props}
              >
                {children}
              </code>
            )

          }


          return (
            <code
              className="font-mono text-[11px] leading-5 text-slate-200"
              {...props}
            >
              {children}
            </code>
          )

        },


        // ----------------------------------------------------
        // Code Blocks
        // ----------------------------------------------------

        pre: ({ children }) => (
          <pre className="my-3 overflow-x-auto rounded-xl bg-slate-950 p-4 text-[11px] leading-5 text-slate-200">
            {children}
          </pre>
        ),


        // ----------------------------------------------------
        // Blockquote
        // ----------------------------------------------------

        blockquote: ({ children }) => (
          <blockquote className="border-l-2 border-blue-300 pl-3 my-3 text-slate-600 italic">
            {children}
          </blockquote>
        ),


        // ----------------------------------------------------
        // Horizontal Rule
        // ----------------------------------------------------

        hr: () => (
          <hr className="my-4 border-slate-200" />
        ),


        // ----------------------------------------------------
        // Links
        // ----------------------------------------------------

        a: ({ children, href }) => (
          <a
            href={href}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 hover:text-blue-700 underline"
          >
            {children}
          </a>
        )

      }}
    >
      {content}
    </ReactMarkdown>
  )

}


// ============================================================
// COMPONENT
// ============================================================

function AICoach() {

  const location = useLocation()

  const messagesEndRef = useRef(null)


  // ==========================================================
  // THREAD ID
  // ==========================================================

  const threadIdRef =
    useRef(crypto.randomUUID())


  // ==========================================================
  // PROBLEM CONTEXT
  // ==========================================================

  const problemContext =
    location.state?.problem || null

  const initialCode =
    location.state?.code || ''

  const initialLanguage =
    location.state?.language || 'java'


  // ==========================================================
  // STATE
  // ==========================================================

  const [selectedMode, setSelectedMode] =
    useState('explain')

  const [language, setLanguage] =
    useState(initialLanguage)

  const [code, setCode] =
    useState(initialCode)

  const [input, setInput] =
    useState('')

  const [messages, setMessages] =
    useState([])

  const [isThinking, setIsThinking] =
    useState(false)

  const [error, setError] =
    useState('')

  const [showContext, setShowContext] =
    useState(false)


  // ==========================================================
  // CURRENT MODE
  // ==========================================================

  const currentMode = useMemo(() => {

    return (
      coachingModes.find(
        (mode) => mode.id === selectedMode
      ) || coachingModes[0]
    )

  }, [selectedMode])


  // ==========================================================
  // PROBLEM CONTEXT STATUS
  // ==========================================================

  const hasProblemContext =
    Boolean(problemContext)


  // ==========================================================
  // WELCOME MESSAGE
  // ==========================================================

  const createWelcomeMessage = () => {

    if (problemContext) {

      return (
        `I’m ready to help you with **${problemContext.title}**. ` +
        `What would you like to work on?`
      )

    }

    return (
      'I’m your DSA Coach. Ask me about a problem, ' +
      'your approach, complexity, or your code.'
    )

  }


  // ==========================================================
  // INITIALIZE CHAT
  // ==========================================================

  useEffect(() => {

    // --------------------------------------------------------
    // New problem = new conversation thread
    // --------------------------------------------------------

    threadIdRef.current =
      crypto.randomUUID()


    setMessages([
      {
        id: `welcome-${Date.now()}`,
        role: 'assistant',
        content: createWelcomeMessage()
      }
    ])


    setError('')
    setInput('')
    setIsThinking(false)
    setShowContext(false)

  }, [problemContext?.id])


  // ==========================================================
  // UPDATE CONTEXT WHEN NAVIGATION STATE CHANGES
  // ==========================================================

  useEffect(() => {

    if (location.state?.code !== undefined) {

      setCode(
        location.state.code || ''
      )

    }


    if (location.state?.language) {

      setLanguage(
        location.state.language
      )

    }

  }, [location.state])


  // ==========================================================
  // SCROLL CHAT
  // ==========================================================

  useEffect(() => {

    messagesEndRef.current?.scrollIntoView({
      behavior: 'smooth'
    })

  }, [messages, isThinking])


  // ==========================================================
  // SEND MESSAGE
  // ==========================================================

  const handleSend = async (
    messageOverride = null
  ) => {

    const message = (
      messageOverride !== null
        ? messageOverride
        : input
    ).trim()


    if (!message || isThinking) {
      return
    }


    setError('')


    // --------------------------------------------------------
    // USER MESSAGE
    // --------------------------------------------------------

    const userMessage = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: message
    }


    setMessages((prev) => [
      ...prev,
      userMessage
    ])


    setInput('')
    setIsThinking(true)


    try {

      // ------------------------------------------------------
      // CONVERSATION
      // ------------------------------------------------------

      const conversation = [
        ...messages,
        userMessage
      ].map((item) => ({
        role: item.role,
        content: item.content
      }))


      // ------------------------------------------------------
      // AI SERVICE
      // ------------------------------------------------------

      const response = await getCoachResponse({

        message,

        mode:
          selectedMode,

        language,

        code,

        problem:
          problemContext,

        conversation,

        thread_id:
          threadIdRef.current

      })


      // ------------------------------------------------------
      // UPDATE THREAD ID
      // ------------------------------------------------------

      if (response?.thread_id) {

        threadIdRef.current =
          response.thread_id

      }


      // ------------------------------------------------------
      // ASSISTANT MESSAGE
      // ------------------------------------------------------

      const assistantMessage = {
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: response.answer
      }


      setMessages((prev) => [
        ...prev,
        assistantMessage
      ])

    }

    catch (err) {

      console.error(
        'AI Coach error:',
        err
      )


      setError(
        err?.message ||
        'Something went wrong while getting a response. Please try again.'
      )

    }

    finally {

      setIsThinking(false)

    }

  }


  // ==========================================================
  // ENTER KEY
  // ==========================================================

  const handleKeyDown = (event) => {

    if (
      event.key === 'Enter' &&
      !event.shiftKey
    ) {

      event.preventDefault()

      handleSend()

    }

  }


  // ==========================================================
  // CLEAR CHAT
  // ==========================================================

  const handleClearChat = () => {

    // --------------------------------------------------------
    // Clearing the visible messages should ALSO create a new
    // LangGraph thread.
    // --------------------------------------------------------

    threadIdRef.current =
      crypto.randomUUID()


    setMessages([
      {
        id: `welcome-${Date.now()}`,
        role: 'assistant',
        content: problemContext
          ? `Let’s start fresh with **${problemContext.title}**. What would you like help with?`
          : 'Let’s start fresh. What would you like help with?'
      }
    ])


    setInput('')
    setError('')

  }


  // ==========================================================
  // CHANGE MODE
  // ==========================================================

  const handleModeChange = (mode) => {

    setSelectedMode(mode)
    setError('')

  }


  // ==========================================================
  // RENDER
  // ==========================================================

  return (

    <div className="max-w-[1450px] mx-auto pb-8">

      {/* ======================================================
          PAGE HEADER
      ====================================================== */}

      <div className="mb-5">

        <div className="flex items-center justify-between gap-4">

          <div>

            <div className="flex items-center gap-2.5">

              <div className="w-9 h-9 rounded-xl bg-blue-600 text-white flex items-center justify-center shadow-sm">

                <Sparkles size={17} />

              </div>


              <div>

                <h1 className="text-xl font-bold tracking-tight text-slate-900">
                  AI Coach
                </h1>

                <p className="mt-0.5 text-xs text-slate-500">
                  Your personal DSA learning assistant
                </p>

              </div>

            </div>

          </div>


          {/* STATUS */}

          <div className="hidden sm:flex items-center gap-2 px-3 py-2 rounded-lg border border-slate-200 bg-white">

            <span
              className={`w-2 h-2 rounded-full ${
                isThinking
                  ? 'bg-blue-500 animate-pulse'
                  : 'bg-emerald-500'
              }`}
            />

            <span className="text-[11px] font-semibold text-slate-600">

              {isThinking
                ? 'Thinking...'
                : 'Ready'}

            </span>

          </div>

        </div>

      </div>


      {/* ======================================================
          MAIN WORKSPACE
      ====================================================== */}

      <div className="grid grid-cols-1 xl:grid-cols-[270px_minmax(0,1fr)] gap-4">


        {/* ====================================================
            LEFT SIDEBAR
        ==================================================== */}

        <aside className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">


          {/* COACHING MODES */}

          <div className="p-4">

            <div className="px-2 mb-3">

              <p className="text-[10px] font-semibold uppercase tracking-[0.12em] text-slate-400">
                Coaching Modes
              </p>

            </div>


            <div className="space-y-1.5">

              {coachingModes.map((mode) => {

                const Icon = mode.icon

                const isActive =
                  selectedMode === mode.id


                return (

                  <button
                    key={mode.id}
                    type="button"
                    onClick={() =>
                      handleModeChange(mode.id)
                    }
                    className={`
                      w-full
                      text-left
                      p-3
                      rounded-xl
                      border
                      transition
                      ${
                        isActive
                          ? 'border-blue-100 bg-blue-50/70'
                          : 'border-transparent hover:border-slate-200 hover:bg-slate-50'
                      }
                    `}
                  >

                    <div className="flex items-start gap-3">

                      <div
                        className={`
                          w-8
                          h-8
                          rounded-lg
                          flex
                          items-center
                          justify-center
                          shrink-0
                          ${
                            isActive
                              ? 'bg-blue-600 text-white'
                              : 'bg-slate-100 text-slate-500'
                          }
                        `}
                      >

                        <Icon size={15} />

                      </div>


                      <div className="min-w-0">

                        <p
                          className={`
                            text-xs
                            font-semibold
                            ${
                              isActive
                                ? 'text-blue-700'
                                : 'text-slate-700'
                            }
                          `}
                        >
                          {mode.label}
                        </p>


                        <p className="mt-0.5 text-[10px] leading-4 text-slate-500">
                          {mode.description}
                        </p>

                      </div>

                    </div>

                  </button>

                )

              })}

            </div>

          </div>


          {/* CURRENT PROBLEM */}

          <div className="border-t border-slate-100 p-4">

            <div className="flex items-center justify-between mb-3">

              <p className="text-[10px] font-semibold uppercase tracking-[0.12em] text-slate-400">
                Current Problem
              </p>


              {hasProblemContext && (

                <Check
                  size={13}
                  className="text-emerald-500"
                />

              )}

            </div>


            {hasProblemContext ? (

              <div className="rounded-xl border border-slate-200 bg-slate-50 p-3">

                <div className="flex items-start gap-2.5">

                  <div className="w-8 h-8 rounded-lg bg-white border border-slate-200 flex items-center justify-center shrink-0">

                    <FileCode2
                      size={15}
                      className="text-blue-600"
                    />

                  </div>


                  <div className="min-w-0">

                    <p className="text-xs font-semibold text-slate-800 truncate">
                      {problemContext.title}
                    </p>


                    <div className="flex items-center gap-2 mt-1">

                      <span className="text-[10px] text-emerald-600 font-medium">
                        {problemContext.difficulty}
                      </span>


                      <span className="text-slate-300">
                        •
                      </span>


                      <span className="text-[10px] text-slate-500">
                        {language}
                      </span>

                    </div>

                  </div>

                </div>

              </div>

            ) : (

              <div className="rounded-xl border border-dashed border-slate-200 p-3">

                <p className="text-[11px] leading-4 text-slate-500">
                  Open a problem from Practice to give your coach more context.
                </p>

              </div>

            )}

          </div>


          {/* CODE CONTEXT */}

          {hasProblemContext && (

            <div className="border-t border-slate-100 p-4">

              <button
                type="button"
                onClick={() =>
                  setShowContext((prev) => !prev)
                }
                className="w-full flex items-center justify-between text-left"
              >

                <div className="flex items-center gap-2">

                  <Code2
                    size={14}
                    className="text-slate-400"
                  />

                  <span className="text-[11px] font-semibold text-slate-600">
                    Code context
                  </span>

                </div>


                <ChevronDown
                  size={14}
                  className={`
                    text-slate-400
                    transition
                    ${
                      showContext
                        ? 'rotate-180'
                        : ''
                    }
                  `}
                />

              </button>


              {showContext && (

                <div className="mt-3">

                  <div className="flex items-center justify-between mb-2">

                    <span className="text-[10px] text-slate-400 uppercase tracking-wider">
                      {language}
                    </span>

                  </div>


                  <pre className="max-h-36 overflow-auto rounded-lg bg-slate-950 p-3 text-[10px] leading-4 text-slate-300 font-mono">
                    {code || 'No code available.'}
                  </pre>

                </div>

              )}

            </div>

          )}

        </aside>


        {/* ====================================================
            CHAT AREA
        ==================================================== */}

        <section className="h-[700px] bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden flex flex-col">


          {/* CHAT HEADER */}

          <div className="h-14 shrink-0 px-5 border-b border-slate-100 flex items-center justify-between">

            <div className="flex items-center gap-3">

              <div className="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center">

                <Bot size={16} />

              </div>


              <div>

                <p className="text-xs font-semibold text-slate-800">
                  DSA Coach
                </p>

                <p className="text-[10px] text-slate-400">
                  {currentMode.label}
                </p>

              </div>

            </div>


            <button
              type="button"
              onClick={handleClearChat}
              className="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-[10px] font-medium text-slate-500 hover:text-slate-700 hover:bg-slate-50 transition"
              title="Clear conversation"
            >

              <RefreshCcw size={12} />

              Clear

            </button>

          </div>


          {/* MESSAGES */}

          <div className="flex-1 min-h-0 overflow-y-auto p-5">

            <div className="max-w-3xl mx-auto space-y-5">

              {messages.map((message) => {

                const isUser =
                  message.role === 'user'


                return (

                  <div
                    key={message.id}
                    className={`
                      flex
                      gap-3
                      ${
                        isUser
                          ? 'justify-end'
                          : 'justify-start'
                      }
                    `}
                  >

                    {!isUser && (

                      <div className="w-7 h-7 rounded-lg bg-blue-600 text-white flex items-center justify-center shrink-0 mt-0.5">

                        <Sparkles size={13} />

                      </div>

                    )}


                    <div
                      className={`
                        max-w-[78%]
                        ${
                          isUser
                            ? 'order-first'
                            : ''
                        }
                      `}
                    >

                      <div
                        className={`
                          rounded-2xl
                          px-4
                          py-3
                          ${
                            isUser
                              ? 'bg-slate-50 border border-slate-200 text-white rounded-tr-md'
                              : 'bg-slate-50 border border-slate-200 text-slate-700 rounded-tl-md'
                          }
                        `}
                      >

                        {/* ------------------------------------------------
                            IMPORTANT:
                            Markdown must NOT be wrapped inside <p>.
                            ReactMarkdown creates its own paragraphs,
                            code blocks, lists, headings, etc.
                        ------------------------------------------------- */}

                        <div
                          className={`
                            text-xs
                            leading-6
                            ${
                              isUser
                                ? 'text-slate-100'
                                : 'text-slate-700'
                            }
                          `}
                        >

                          {renderMessageContent(
                            message.content
                          )}

                        </div>

                      </div>


                      <p
                        className={`
                          mt-1.5
                          text-[9px]
                          text-slate-400
                          ${
                            isUser
                              ? 'text-right'
                              : 'text-left'
                          }
                        `}
                      >

                        {isUser
                          ? 'You'
                          : 'AI Coach'}

                      </p>

                    </div>


                    {isUser && (

                      <div className="w-7 h-7 rounded-lg bg-slate-100 text-slate-500 flex items-center justify-center shrink-0 mt-0.5">

                        <MessageCircle size={13} />

                      </div>

                    )}

                  </div>

                )

              })}


              {/* THINKING */}

              {isThinking && (

                <div className="flex items-start gap-3">

                  <div className="w-7 h-7 rounded-lg bg-blue-600 text-white flex items-center justify-center shrink-0">

                    <Sparkles size={13} />

                  </div>


                  <div className="rounded-2xl rounded-tl-md bg-slate-50 border border-slate-200 px-4 py-3">

                    <div className="flex items-center gap-1.5">

                      <span className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce" />


                      <span
                        className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce"
                        style={{
                          animationDelay: '120ms'
                        }}
                      />


                      <span
                        className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce"
                        style={{
                          animationDelay: '240ms'
                        }}
                      />

                    </div>

                  </div>

                </div>

              )}


              {/* ERROR */}

              {error && (

                <div className="rounded-xl border border-red-200 bg-red-50 p-3">

                  <div className="flex items-start gap-2">

                    <X
                      size={14}
                      className="text-red-500 mt-0.5"
                    />


                    <p className="text-xs text-red-600">
                      {error}
                    </p>

                  </div>

                </div>

              )}


              <div ref={messagesEndRef} />

            </div>

          </div>


          {/* QUICK PROMPTS */}

          <div className="px-5 pb-3">

            <div className="max-w-3xl mx-auto">

              <div className="flex items-center gap-2 overflow-x-auto pb-1">

                {quickPrompts.map((prompt) => (

                  <button
                    key={prompt}
                    type="button"
                    disabled={isThinking}
                    onClick={() =>
                      handleSend(prompt)
                    }
                    className="shrink-0 px-3 py-1.5 rounded-lg border border-slate-200 bg-white text-[10px] font-medium text-slate-500 hover:border-blue-200 hover:text-blue-600 hover:bg-blue-50/40 disabled:opacity-50 transition"
                  >
                    {prompt}
                  </button>

                ))}

              </div>

            </div>

          </div>


          {/* INPUT */}

          <div className="px-5 pb-5">

            <div className="max-w-3xl mx-auto">

              <div className="relative rounded-xl border border-slate-200 bg-white shadow-sm focus-within:border-blue-300 focus-within:ring-2 focus-within:ring-blue-50 transition">

                <textarea
                  value={input}
                  onChange={(event) =>
                    setInput(event.target.value)
                  }
                  onKeyDown={handleKeyDown}
                  placeholder="Ask your coach anything..."
                  rows={2}
                  disabled={isThinking}
                  className="w-full resize-none bg-white px-4 py-3 pr-14 text-xs text-slate-700 placeholder:text-slate-400 outline-none disabled:bg-white"
                />


                <button
                  type="button"
                  onClick={() =>
                    handleSend()
                  }
                  disabled={
                    !input.trim() ||
                    isThinking
                  }
                  className="absolute right-3 bottom-3 w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center hover:bg-blue-500 disabled:bg-slate-200 disabled:text-slate-400 transition"
                  title="Send message"
                >

                  <Send size={14} />

                </button>

              </div>


              <div className="flex items-center justify-between mt-2 px-1">

                <p className="text-[9px] text-slate-400">
                  AI Coach can make mistakes. Use it as a learning assistant.
                </p>


                {hasProblemContext && (

                  <div className="hidden sm:flex items-center gap-1.5 text-[9px] text-slate-400">

                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />

                    Problem context attached

                  </div>

                )}

              </div>

            </div>

          </div>

        </section>

      </div>

    </div>

  )

}


export default AICoach