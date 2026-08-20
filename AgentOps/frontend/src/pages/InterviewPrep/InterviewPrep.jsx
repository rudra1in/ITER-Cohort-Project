import {
  useEffect,
  useMemo,
  useState
} from 'react'

import {
  ArrowRight,
  Award,
  BarChart3,
  Brain,
  BriefcaseBusiness,
  Check,
  ChevronDown,
  ChevronRight,
  Clock3,
  Code2,
  Database,
  FileText,
  Flame,
  Lightbulb,
  MessageCircle,
  Play,
  RotateCcw,
  Search,
  Sparkles,
  Target,
  Trophy,
  Users,
  X,
  Zap
} from 'lucide-react'

import {
  getInterviewCategories,
  getInterviewQuestions,
  getInterviewStats,
  getMockInterviewQuestions
} from '../../services/interviewPrepService'


// ============================================================
// CATEGORY ICONS
// ============================================================

const categoryIcons = {

  'Technical Interview': Code2,

  'DSA Interview': Brain,

  'SQL & DBMS': Database,

  'CS Fundamentals': FileText,

  'HR & Behavioral': Users

}


// ============================================================
// DIFFICULTY STYLES
// ============================================================

const difficultyStyles = {

  Easy: {
    text: 'text-emerald-600',
    bg: 'bg-emerald-50',
    border: 'border-emerald-100'
  },

  Medium: {
    text: 'text-amber-600',
    bg: 'bg-amber-50',
    border: 'border-amber-100'
  },

  Hard: {
    text: 'text-red-600',
    bg: 'bg-red-50',
    border: 'border-red-100'
  }

}


// ============================================================
// COMPONENT
// ============================================================

function InterviewPrep() {

  // ==========================================================
  // DATA STATE
  // ==========================================================

  const [categories, setCategories] =
    useState([])

  const [questions, setQuestions] =
    useState([])

  const [stats, setStats] =
    useState(null)

  const [isLoading, setIsLoading] =
    useState(true)


  // ==========================================================
  // FILTER STATE
  // ==========================================================

  const [selectedCategory, setSelectedCategory] =
    useState('All')

  const [selectedDifficulty, setSelectedDifficulty] =
    useState('All')

  const [searchQuery, setSearchQuery] =
    useState('')


  // ==========================================================
  // QUESTION STATE
  // ==========================================================

  const [expandedQuestion, setExpandedQuestion] =
    useState(null)

  const [completedQuestions, setCompletedQuestions] =
    useState(() => {

      try {

        const saved =
          localStorage.getItem(
            'dsaCoachInterviewCompleted'
          )

        const parsed =
          saved
            ? JSON.parse(saved)
            : []

        return Array.isArray(parsed)
          ? parsed
          : []

      } catch {

        return []

      }

    })


  // ==========================================================
  // MOCK INTERVIEW STATE
  // ==========================================================

  const [showMockInterview, setShowMockInterview] =
    useState(false)

  const [mockQuestions, setMockQuestions] =
    useState([])

  const [mockIndex, setMockIndex] =
    useState(0)

  const [mockStarted, setMockStarted] =
    useState(false)

  const [mockFinished, setMockFinished] =
    useState(false)

  const [mockAnswers, setMockAnswers] =
    useState([])

  const [mockAnswer, setMockAnswer] =
    useState('')

  const [mockRole, setMockRole] =
    useState('Software Developer')

  const [mockDifficulty, setMockDifficulty] =
    useState('Mixed')

  const [isStartingMock, setIsStartingMock] =
    useState(false)


  // ==========================================================
  // LOAD INTERVIEW DATA
  // ==========================================================

  useEffect(() => {

    let mounted = true


    const loadInterviewData = async () => {

      try {

        const [
          categoryData,
          questionData,
          statsData
        ] = await Promise.all([

          getInterviewCategories(),

          getInterviewQuestions(),

          getInterviewStats()

        ])


        if (!mounted) {
          return
        }


        setCategories(
          Array.isArray(categoryData)
            ? categoryData
            : []
        )


        setQuestions(
          Array.isArray(questionData)
            ? questionData
            : []
        )


        setStats(
          statsData || {}
        )

      } catch (error) {

        console.error(
          'Interview Prep loading error:',
          error
        )

      } finally {

        if (mounted) {
          setIsLoading(false)
        }

      }

    }


    loadInterviewData()


    return () => {

      mounted = false

    }

  }, [])


  // ==========================================================
  // SAVE COMPLETED QUESTIONS
  // ==========================================================

  useEffect(() => {

    localStorage.setItem(
      'dsaCoachInterviewCompleted',
      JSON.stringify(completedQuestions)
    )

  }, [
    completedQuestions
  ])


  // ==========================================================
  // FILTER QUESTIONS
  // ==========================================================

  const filteredQuestions =
    useMemo(() => {

      const query =
        searchQuery
          .trim()
          .toLowerCase()


      return questions.filter(
        (question) => {

          const matchesCategory =
            selectedCategory === 'All' ||
            question.category === selectedCategory


          const matchesDifficulty =
            selectedDifficulty === 'All' ||
            question.difficulty === selectedDifficulty


          const questionText =
            String(
              question.question || ''
            ).toLowerCase()


          const topic =
            String(
              question.topic || ''
            ).toLowerCase()


          const matchesSearch =
            !query ||
            questionText.includes(query) ||
            topic.includes(query)


          return (
            matchesCategory &&
            matchesDifficulty &&
            matchesSearch
          )

        }
      )

    }, [
      questions,
      selectedCategory,
      selectedDifficulty,
      searchQuery
    ])


  // ==========================================================
  // COMPLETION HELPERS
  // ==========================================================

  const isCompleted = (id) => {

    return completedQuestions.includes(id)

  }


  const toggleCompleted = (id) => {

    setCompletedQuestions(
      (previous) => {

        if (previous.includes(id)) {

          return previous.filter(
            (item) => item !== id
          )

        }


        return [
          ...previous,
          id
        ]

      }
    )

  }


  // ==========================================================
  // COMPLETION PERCENTAGE
  // ==========================================================

  const completionPercentage =
    useMemo(() => {

      if (!questions.length) {
        return 0
      }


      return Math.min(
        100,
        Math.round(
          (
            completedQuestions.length /
            questions.length
          ) * 100
        )
      )

    }, [
      questions.length,
      completedQuestions.length
    ])


  // ==========================================================
  // START MOCK INTERVIEW
  // ==========================================================

  const startMockInterview =
    async () => {

      if (isStartingMock) {
        return
      }


      setIsStartingMock(true)


      try {

        const data =
          await getMockInterviewQuestions({

            role:
              mockRole,

            difficulty:
              mockDifficulty,

            count:
              5

          })


        if (
          !Array.isArray(data) ||
          data.length === 0
        ) {

          throw new Error(
            'No mock interview questions available.'
          )

        }


        setMockQuestions(data)

        setMockIndex(0)

        setMockAnswers([])

        setMockAnswer('')

        setMockFinished(false)

        setMockStarted(true)


      } catch (error) {

        console.error(
          'Mock interview error:',
          error
        )

      } finally {

        setIsStartingMock(false)

      }

    }


  // ==========================================================
  // SUBMIT MOCK ANSWER
  // ==========================================================

  const submitMockAnswer = () => {

    if (!mockAnswer.trim()) {
      return
    }


    const currentQuestion =
      mockQuestions[mockIndex]


    if (!currentQuestion) {
      return
    }


    const answer = {

      questionId:
        currentQuestion.id,

      question:
        currentQuestion.question,

      answer:
        mockAnswer.trim()

    }


    setMockAnswers(
      (previous) => [
        ...previous,
        answer
      ]
    )


    setMockAnswer('')


    if (
      mockIndex <
      mockQuestions.length - 1
    ) {

      setMockIndex(
        (previous) =>
          previous + 1
      )

    } else {

      setMockFinished(true)


      const currentCount =
        Number(
          localStorage.getItem(
            'dsaCoachMockInterviewCount'
          ) || 0
        )


      localStorage.setItem(
        'dsaCoachMockInterviewCount',
        String(
          currentCount + 1
        )
      )

    }

  }


  // ==========================================================
  // CLOSE MOCK INTERVIEW
  // ==========================================================

  const closeMockInterview = () => {

    setShowMockInterview(false)

    setMockStarted(false)

    setMockFinished(false)

    setMockQuestions([])

    setMockAnswers([])

    setMockAnswer('')

    setMockIndex(0)

  }


  // ==========================================================
  // LOADING STATE
  // ==========================================================

  if (isLoading) {

    return (

      <div className="max-w-[1450px] mx-auto pb-8">

        <div className="animate-pulse space-y-4">

          <div className="h-20 rounded-2xl bg-slate-100" />

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">

            {[
              1,
              2,
              3,
              4
            ].map((item) => (

              <div
                key={item}
                className="h-24 rounded-2xl bg-slate-100"
              />

            ))}

          </div>

          <div className="h-72 rounded-2xl bg-slate-100" />

        </div>

      </div>

    )

  }


  // ==========================================================
  // MAIN UI
  // ==========================================================

  return (

    <div className="max-w-[1450px] mx-auto pb-8">

      {/* ======================================================
          HEADER
      ====================================================== */}

      <div className="mb-5">

        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

          <div>

            <div className="flex items-center gap-2.5">

              <div className="w-9 h-9 rounded-xl bg-blue-600 text-white flex items-center justify-center shadow-sm">

                <BriefcaseBusiness
                  size={17}
                />

              </div>


              <div>

                <h1 className="text-xl font-bold tracking-tight text-slate-900">

                  Interview Prep

                </h1>


                <p className="mt-0.5 text-xs text-slate-500">

                  Prepare for technical, DSA, SQL, and behavioral interviews.

                </p>

              </div>

            </div>

          </div>


          <button
            type="button"
            onClick={() =>
              setShowMockInterview(true)
            }
            className="inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-blue-600 text-white text-xs font-semibold hover:bg-blue-500 transition shadow-sm"
          >

            <Play size={14} />

            Start Mock Interview

          </button>

        </div>

      </div>


      {/* ======================================================
          HERO
      ====================================================== */}

      <section className="relative overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm mb-5">

        <div className="absolute -right-20 -top-24 w-64 h-64 rounded-full bg-blue-50" />


        <div className="relative grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-6 p-6">

          <div>

            <div className="inline-flex items-center gap-1.5 px-2 py-1 rounded-md bg-blue-50 text-blue-600 text-[9px] font-semibold uppercase tracking-wider">

              <Sparkles size={11} />

              Placement Ready

            </div>


            <h2 className="mt-3 text-2xl font-bold tracking-tight text-slate-900">

              Practice the questions recruiters actually ask.

            </h2>


            <p className="mt-2 max-w-2xl text-xs leading-5 text-slate-500">

              Build confidence across DSA, technical interviews, SQL, DBMS, CS fundamentals, and HR questions.

            </p>


            <div className="mt-5 flex flex-wrap gap-2">

              <button
                type="button"
                onClick={() => {
                  setSelectedCategory('DSA Interview')
                  setSearchQuery('')
                }}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-900 text-white text-[10px] font-semibold hover:bg-slate-800 transition"
              >

                <Brain size={12} />

                Practice DSA

              </button>


              <button
                type="button"
                onClick={() => {
                  setSelectedCategory('SQL & DBMS')
                  setSearchQuery('')
                }}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-slate-200 bg-white text-slate-600 text-[10px] font-semibold hover:border-blue-200 hover:text-blue-600 transition"
              >

                <Database size={12} />

                Practice SQL

              </button>

            </div>

          </div>


          <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">

            <div className="flex items-center justify-between">

              <div>

                <p className="text-[10px] uppercase tracking-[0.12em] font-semibold text-slate-400">

                  Interview Progress

                </p>


                <p className="mt-1 text-2xl font-bold text-slate-900">

                  {completionPercentage}%

                </p>

              </div>


              <div className="w-11 h-11 rounded-xl bg-white border border-slate-200 flex items-center justify-center">

                <Trophy
                  size={20}
                  className="text-blue-600"
                />

              </div>

            </div>


            <div className="mt-4 h-2 rounded-full bg-slate-200 overflow-hidden">

              <div
                className="h-full rounded-full bg-blue-600 transition-all"
                style={{
                  width:
                    `${completionPercentage}%`
                }}
              />

            </div>


            <p className="mt-2 text-[10px] text-slate-400">

              {completedQuestions.length}
              {' '}of{' '}
              {questions.length}
              {' '}questions completed

            </p>

          </div>

        </div>

      </section>


      {/* ======================================================
          STATS
      ====================================================== */}

      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-5">

        <StatCard
          icon={Target}
          label="Questions Practiced"
          value={
            stats?.questionsPracticed ??
            completedQuestions.length
          }
        />


        <StatCard
          icon={Check}
          label="Accuracy"
          value={
            stats?.accuracy ??
            0
          }
          suffix="%"
        />


        <StatCard
          icon={Flame}
          label="Current Streak"
          value={
            stats?.streak ??
            0
          }
          suffix=" days"
        />


        <StatCard
          icon={Award}
          label="Mock Interviews"
          value={
            stats?.mockInterviews ??
            0
          }
        />

      </div>


      {/* ======================================================
          CATEGORIES
      ====================================================== */}

      <section className="mb-5">

        <div className="mb-3">

          <h2 className="text-sm font-bold text-slate-800">

            Practice by Category

          </h2>


          <p className="mt-0.5 text-[10px] text-slate-400">

            Focus on the areas most likely to appear in placements.

          </p>

        </div>


        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">

          {categories.map(
            (category) => {

              const Icon =
                categoryIcons[
                  category.name
                ] || Brain


              const active =
                selectedCategory ===
                category.name


              return (

                <button
                  key={category.id}
                  type="button"
                  onClick={() => {

                    setSelectedCategory(
                      active
                        ? 'All'
                        : category.name
                    )

                    setSearchQuery('')

                  }}
                  className={`text-left rounded-2xl border p-4 transition ${
                    active
                      ? 'border-blue-200 bg-blue-50/60'
                      : 'border-slate-200 bg-white hover:border-blue-100 hover:bg-slate-50'
                  }`}
                >

                  <div className="flex items-start gap-3">

                    <div className={`w-9 h-9 rounded-xl flex items-center justify-center shrink-0 ${
                      active
                        ? 'bg-blue-600 text-white'
                        : 'bg-slate-100 text-slate-500'
                    }`}>

                      <Icon size={16} />

                    </div>


                    <div className="min-w-0 flex-1">

                      <div className="flex items-center justify-between gap-2">

                        <p className={`text-xs font-semibold ${
                          active
                            ? 'text-blue-700'
                            : 'text-slate-800'
                        }`}>

                          {category.name}

                        </p>


                        <ChevronRight
                          size={13}
                          className="text-slate-300"
                        />

                      </div>


                      <p className="mt-1 text-[10px] leading-4 text-slate-500">

                        {category.description}

                      </p>


                      <p className="mt-2 text-[9px] font-medium text-slate-400">

                        {category.questionCount}
                        {' '}practice questions

                      </p>

                    </div>

                  </div>

                </button>

              )

            }
          )}

        </div>

      </section>


      {/* ======================================================
          QUESTION BANK
      ====================================================== */}

      <section>

        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3 mb-3">

          <div>

            <h2 className="text-sm font-bold text-slate-800">

              Interview Question Bank

            </h2>


            <p className="mt-0.5 text-[10px] text-slate-400">

              Expand a question to review the answer and key points.

            </p>

          </div>


          <div className="flex flex-col sm:flex-row gap-2">

            <div className="relative">

              <Search
                size={13}
                className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
              />


              <input
                type="text"
                value={searchQuery}
                onChange={(event) =>
                  setSearchQuery(
                    event.target.value
                  )
                }
                placeholder="Search questions..."
                className="w-full sm:w-56 h-9 rounded-lg border border-slate-200 bg-white pl-8 pr-3 text-[10px] text-slate-700 outline-none focus:border-blue-300 focus:ring-2 focus:ring-blue-50"
              />

            </div>


            <FilterSelect
              value={selectedCategory}
              onChange={setSelectedCategory}
              options={[
                'All',
                ...categories.map(
                  (category) =>
                    category.name
                )
              ]}
            />


            <FilterSelect
              value={selectedDifficulty}
              onChange={setSelectedDifficulty}
              options={[
                'All',
                'Easy',
                'Medium',
                'Hard'
              ]}
            />

          </div>

        </div>


        <div className="space-y-2.5">

          {filteredQuestions.length === 0 ? (

            <div className="rounded-2xl border border-dashed border-slate-200 bg-white p-10 text-center">

              <Search
                size={22}
                className="mx-auto text-slate-300"
              />


              <p className="mt-3 text-xs font-semibold text-slate-700">

                No questions found

              </p>


              <p className="mt-1 text-[10px] text-slate-400">

                Try changing your search or filters.

              </p>


              <button
                type="button"
                onClick={() => {

                  setSearchQuery('')
                  setSelectedCategory('All')
                  setSelectedDifficulty('All')

                }}
                className="mt-4 px-3 py-1.5 rounded-lg bg-slate-900 text-white text-[10px] font-semibold"
              >

                Clear Filters

              </button>

            </div>

          ) : (

            filteredQuestions.map(
              (question) => {

                const completed =
                  isCompleted(
                    question.id
                  )


                const expanded =
                  expandedQuestion ===
                  question.id


                const difficulty =
                  difficultyStyles[
                    question.difficulty
                  ] ||
                  difficultyStyles.Easy


                return (

                  <div
                    key={question.id}
                    className={`rounded-2xl border bg-white overflow-hidden transition ${
                      completed
                        ? 'border-emerald-100'
                        : 'border-slate-200'
                    }`}
                  >

                    <div className="p-4 flex items-start gap-3">

                      <button
                        type="button"
                        onClick={() =>
                          toggleCompleted(
                            question.id
                          )
                        }
                        className={`w-7 h-7 rounded-lg border flex items-center justify-center shrink-0 transition ${
                          completed
                            ? 'bg-emerald-500 border-emerald-500 text-white'
                            : 'border-slate-200 text-transparent hover:border-blue-300'
                        }`}
                        title={
                          completed
                            ? 'Mark incomplete'
                            : 'Mark complete'
                        }
                      >

                        <Check size={13} />

                      </button>


                      <div className="min-w-0 flex-1">

                        <div className="flex flex-wrap items-center gap-2">

                          <span className="text-[9px] font-semibold uppercase tracking-wider text-blue-600">

                            {question.category}

                          </span>


                          <span className="text-slate-300">
                            •
                          </span>


                          <span className="text-[9px] text-slate-400">

                            {question.topic}

                          </span>

                        </div>


                        <button
                          type="button"
                          onClick={() =>
                            setExpandedQuestion(
                              expanded
                                ? null
                                : question.id
                            )
                          }
                          className="mt-1 flex items-start justify-between gap-3 w-full text-left text-xs font-semibold leading-5 text-slate-800 hover:text-blue-600"
                        >

                          <span>
                            {question.question}
                          </span>


                          <ChevronDown
                            size={14}
                            className={`shrink-0 mt-0.5 text-slate-400 transition ${
                              expanded
                                ? 'rotate-180'
                                : ''
                            }`}
                          />

                        </button>


                        <div className="mt-2 flex flex-wrap items-center gap-2">

                          <span className={`inline-flex items-center px-2 py-1 rounded-md border text-[9px] font-semibold ${difficulty.text} ${difficulty.bg} ${difficulty.border}`}>

                            {question.difficulty}

                          </span>


                          {completed && (

                            <span className="inline-flex items-center gap-1 text-[9px] font-semibold text-emerald-600">

                              <Check size={10} />

                              Completed

                            </span>

                          )}

                        </div>


                        {expanded && (

                          <div className="mt-4 pt-4 border-t border-slate-100">

                            <div className="rounded-xl bg-slate-50 border border-slate-200 p-4">

                              <div className="flex items-center gap-2 mb-2">

                                <MessageCircle
                                  size={13}
                                  className="text-blue-500"
                                />


                                <span className="text-[10px] font-semibold uppercase tracking-wider text-slate-500">

                                  Suggested Answer

                                </span>

                              </div>


                              <p className="text-[11px] leading-5 text-slate-600">

                                {question.answer}

                              </p>

                            </div>


                            {Array.isArray(
                              question.keyPoints
                            ) &&
                            question.keyPoints.length > 0 && (

                              <div className="mt-3 rounded-xl border border-slate-200 p-4">

                                <div className="flex items-center gap-2 mb-2">

                                  <Zap
                                    size={13}
                                    className="text-blue-500"
                                  />


                                  <span className="text-[10px] font-semibold uppercase tracking-wider text-slate-500">

                                    Key Points

                                  </span>

                                </div>


                                <ul className="space-y-2">

                                  {question.keyPoints.map(
                                    (point) => (

                                      <li
                                        key={point}
                                        className="flex items-start gap-2 text-[11px] leading-4 text-slate-600"
                                      >

                                        <span className="w-1.5 h-1.5 rounded-full bg-blue-400 mt-1.5 shrink-0" />


                                        <span>
                                          {point}
                                        </span>

                                      </li>

                                    )
                                  )}

                                </ul>

                              </div>

                            )}


                            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 mt-4 pt-3 border-t border-slate-200">

                              <p className="text-[9px] text-slate-400">

                                {completed
                                  ? 'You have completed this question.'
                                  : 'Practice answering this question out loud before marking it complete.'}

                              </p>


                              <button
                                type="button"
                                onClick={() =>
                                  toggleCompleted(
                                    question.id
                                  )
                                }
                                className={`shrink-0 inline-flex items-center justify-center gap-1.5 px-3 py-1.5 rounded-lg text-[10px] font-semibold transition ${
                                  completed
                                    ? 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
                                    : 'bg-blue-600 text-white hover:bg-blue-500'
                                }`}
                              >

                                {completed ? (

                                  <>

                                    <RotateCcw
                                      size={11}
                                    />

                                    Mark incomplete

                                  </>

                                ) : (

                                  <>

                                    <Check
                                      size={11}
                                    />

                                    Mark complete

                                  </>

                                )}

                              </button>

                            </div>

                          </div>

                        )}

                      </div>

                    </div>

                  </div>

                )

              }
            )

          )}

        </div>

      </section>


      {/* ======================================================
          MOCK INTERVIEW MODAL
      ====================================================== */}

      {showMockInterview && (

        <div
          className="fixed inset-0 z-50 bg-slate-950/40 backdrop-blur-sm flex items-center justify-center p-4"
          onMouseDown={(event) => {

            if (
              event.target ===
              event.currentTarget
            ) {

              closeMockInterview()

            }

          }}
        >

          <div className="w-full max-w-2xl max-h-[90vh] overflow-y-auto rounded-2xl border border-slate-200 bg-white shadow-2xl">

            {/* ------------------------------------------------
                MODAL HEADER
            ------------------------------------------------ */}

            <div className="flex items-center justify-between gap-4 px-5 py-4 border-b border-slate-100">

              <div className="flex items-center gap-3">

                <div className="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">

                  <BriefcaseBusiness
                    size={17}
                  />

                </div>


                <div>

                  <p className="text-xs font-bold text-slate-800">

                    Mock Interview

                  </p>


                  <p className="text-[10px] text-slate-400">

                    Simulate a real interview session

                  </p>

                </div>

              </div>


              <button
                type="button"
                onClick={closeMockInterview}
                className="w-8 h-8 rounded-lg flex items-center justify-center text-slate-400 hover:bg-slate-50 hover:text-slate-700"
              >

                <X size={15} />

              </button>

            </div>


            {/* ------------------------------------------------
                SETUP
            ------------------------------------------------ */}

            {!mockStarted && !mockFinished && (

              <div className="p-5">

                <div className="rounded-2xl bg-slate-50 border border-slate-200 p-5">

                  <div className="flex items-center gap-2">

                    <Target
                      size={16}
                      className="text-blue-600"
                    />


                    <h3 className="text-sm font-bold text-slate-800">

                      Configure your interview

                    </h3>

                  </div>


                  <p className="mt-1 text-[10px] leading-4 text-slate-500">

                    Choose the type of interview you want to practice.

                  </p>


                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-5">

                    <div>

                      <label className="block mb-1.5 text-[10px] font-semibold text-slate-500">

                        Target Role

                      </label>


                      <select
                        value={mockRole}
                        onChange={(event) =>
                          setMockRole(
                            event.target.value
                          )
                        }
                        className="w-full h-10 rounded-lg border border-slate-200 bg-white px-3 text-[10px] text-slate-700 outline-none focus:border-blue-300"
                      >

                        <option>
                          Software Developer
                        </option>

                        <option>
                          Product Analyst
                        </option>

                        <option>
                          Backend Developer
                        </option>

                        <option>
                          Full Stack Developer
                        </option>

                        <option>
                          Data Analyst
                        </option>

                      </select>

                    </div>


                    <div>

                      <label className="block mb-1.5 text-[10px] font-semibold text-slate-500">

                        Difficulty

                      </label>


                      <select
                        value={mockDifficulty}
                        onChange={(event) =>
                          setMockDifficulty(
                            event.target.value
                          )
                        }
                        className="w-full h-10 rounded-lg border border-slate-200 bg-white px-3 text-[10px] text-slate-700 outline-none focus:border-blue-300"
                      >

                        <option>
                          Mixed
                        </option>

                        <option>
                          Easy
                        </option>

                        <option>
                          Medium
                        </option>

                        <option>
                          Hard
                        </option>

                      </select>

                    </div>

                  </div>


                  <div className="mt-4 grid grid-cols-3 gap-2">

                    <MockInfo
                      icon={MessageCircle}
                      value="5"
                      label="Questions"
                    />

                    <MockInfo
                      icon={Clock3}
                      value="~10"
                      label="Minutes"
                    />

                    <MockInfo
                      icon={Sparkles}
                      value="AI"
                      label="Ready later"
                    />

                  </div>


                  <button
                    type="button"
                    onClick={startMockInterview}
                    disabled={isStartingMock}
                    className="mt-5 w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-lg bg-blue-600 text-white text-xs font-semibold hover:bg-blue-500 disabled:bg-slate-200 disabled:text-slate-400 transition"
                  >

                    <Play size={13} />

                    {isStartingMock
                      ? 'Preparing Interview...'
                      : 'Begin Interview'}

                  </button>

                </div>

              </div>

            )}


            {/* ------------------------------------------------
                MOCK QUESTIONS
            ------------------------------------------------ */}

            {mockStarted &&
            !mockFinished && (

              <div className="p-5">

                <div className="flex items-center justify-between mb-4">

                  <span className="text-[10px] font-semibold text-blue-600">

                    Question {mockIndex + 1}
                    {' '}of{' '}
                    {mockQuestions.length}

                  </span>


                  <span className="text-[10px] text-slate-400">

                    {mockRole}

                  </span>

                </div>


                <div className="h-1.5 rounded-full bg-slate-100 overflow-hidden mb-5">

                  <div
                    className="h-full bg-blue-600 rounded-full transition-all"
                    style={{
                      width:
                        `${(
                          (
                            mockIndex + 1
                          ) /
                          mockQuestions.length
                        ) * 100}%`
                    }}
                  />

                </div>


                <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">

                  <div className="flex flex-wrap items-center gap-2">

                    <span className="text-[9px] font-semibold uppercase tracking-wider text-blue-600">

                      {mockQuestions[
                        mockIndex
                      ]?.category}

                    </span>


                    <span className="text-slate-300">
                      •
                    </span>


                    <span className="text-[9px] text-slate-400">

                      {mockQuestions[
                        mockIndex
                      ]?.topic}

                    </span>

                  </div>


                  <h3 className="mt-3 text-sm font-bold leading-6 text-slate-800">

                    {mockQuestions[
                      mockIndex
                    ]?.question}

                  </h3>


                  <div className="mt-5">

                    <label className="block mb-2 text-[10px] font-semibold text-slate-500">

                      Your answer

                    </label>


                    <textarea
                      value={mockAnswer}
                      onChange={(event) =>
                        setMockAnswer(
                          event.target.value
                        )
                      }
                      placeholder="Explain your answer as if you were speaking to an interviewer..."
                      rows={6}
                      onKeyDown={(event) => {

                        if (
                          event.key === 'Enter' &&
                          event.ctrlKey
                        ) {

                          event.preventDefault()

                          submitMockAnswer()

                        }

                      }}
                      className="w-full resize-none rounded-xl border border-slate-200 bg-white p-3 text-xs leading-5 text-slate-700 placeholder:text-slate-400 outline-none focus:border-blue-300 focus:ring-2 focus:ring-blue-50"
                    />

                  </div>


                  <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 mt-3">

                    <p className="text-[9px] text-slate-400">

                      Take your time. Explain your reasoning clearly.

                    </p>


                    <button
                      type="button"
                      disabled={
                        !mockAnswer.trim()
                      }
                      onClick={
                        submitMockAnswer
                      }
                      className="inline-flex items-center justify-center gap-2 px-4 py-2 rounded-lg bg-blue-600 text-white text-[10px] font-semibold hover:bg-blue-500 disabled:bg-slate-200 disabled:text-slate-400 transition"
                    >

                      {mockIndex ===
                      mockQuestions.length - 1
                        ? 'Finish Interview'
                        : 'Submit Answer'}

                      <ArrowRight
                        size={12}
                      />

                    </button>

                  </div>

                </div>

              </div>

            )}


            {/* ------------------------------------------------
                MOCK FINISHED
            ------------------------------------------------ */}

            {mockFinished && (

              <div className="p-6 text-center">

                <div className="mx-auto w-14 h-14 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center">

                  <Trophy size={25} />

                </div>


                <h3 className="mt-4 text-lg font-bold text-slate-900">

                  Mock Interview Complete

                </h3>


                <p className="mt-1 text-xs leading-5 text-slate-500 max-w-md mx-auto">

                  Great job completing the interview. Your answers are stored in the session and are ready for AI evaluation once the Interview Agent is connected.

                </p>


                <div className="grid grid-cols-3 gap-2 max-w-sm mx-auto mt-5">

                  <MockInfo
                    icon={Check}
                    value={
                      mockAnswers.length
                    }
                    label="Answered"
                  />


                  <MockInfo
                    icon={Clock3}
                    value="Done"
                    label="Status"
                  />


                  <MockInfo
                    icon={Sparkles}
                    value="AI"
                    label="Evaluation"
                  />

                </div>


                <button
                  type="button"
                  onClick={closeMockInterview}
                  className="mt-5 px-5 py-2.5 rounded-lg bg-slate-900 text-white text-xs font-semibold hover:bg-slate-800 transition"
                >

                  Back to Interview Prep

                </button>

              </div>

            )}

          </div>

        </div>

      )}

    </div>

  )

}


// ============================================================
// STAT CARD
// ============================================================

function StatCard({
  icon: Icon,
  label,
  value,
  suffix = ''
}) {

  return (

    <div className="bg-white border border-slate-200 rounded-2xl p-4 shadow-sm">

      <div className="flex items-center justify-between">

        <div className="w-8 h-8 rounded-lg bg-slate-50 text-slate-500 flex items-center justify-center">

          <Icon size={14} />

        </div>


        <BarChart3
          size={12}
          className="text-slate-300"
        />

      </div>


      <p className="mt-3 text-lg font-bold text-slate-900">

        {value}
        {suffix}

      </p>


      <p className="mt-0.5 text-[10px] text-slate-400">

        {label}

      </p>

    </div>

  )

}


// ============================================================
// FILTER SELECT
// ============================================================

function FilterSelect({
  value,
  onChange,
  options
}) {

  return (

    <div className="relative">

      <select
        value={value}
        onChange={(event) =>
          onChange(
            event.target.value
          )
        }
        className="h-9 min-w-[130px] appearance-none rounded-lg border border-slate-200 bg-white pl-3 pr-8 text-[10px] font-medium text-slate-600 outline-none focus:border-blue-300 focus:ring-2 focus:ring-blue-50"
      >

        {options.map(
          (option) => (

            <option
              key={option}
              value={option}
            >
              {option}
            </option>

          )
        )}

      </select>


      <ChevronDown
        size={12}
        className="pointer-events-none absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400"
      />

    </div>

  )

}


// ============================================================
// MOCK INFO
// ============================================================

function MockInfo({
  icon: Icon,
  value,
  label
}) {

  return (

    <div className="rounded-xl border border-slate-200 bg-white p-3 text-center">

      <div className="flex items-center justify-center">

        <Icon
          size={13}
          className="text-blue-500"
        />

      </div>


      <p className="mt-1 text-xs font-bold text-slate-800">

        {value}

      </p>


      <p className="mt-0.5 text-[9px] text-slate-400">

        {label}

      </p>

    </div>

  )

}


export default InterviewPrep