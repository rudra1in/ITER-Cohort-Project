import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import {
  ArrowLeft,
  Timer,
  RotateCcw,
  Sparkles,
  HelpCircle,
  ArrowRight,
  Check,
  CheckCircle2,
  XCircle,
  Award,
  Clock
} from 'lucide-react'

// ==========================================
// 1. MCQ DATABASE
// ==========================================
const MCQ_DATABASE = [
  {
    id: 1,
    question: "What is the average time complexity of searching in a hash table?",
    options: [
      { key: "A", text: "O(n)" },
      { key: "B", text: "O(log n)" },
      { key: "C", text: "O(1)" },
      { key: "D", text: "O(n log n)" }
    ],
    correct_answer: "C",
    explanation: "Hash tables achieve average O(1) time complexity for lookup operations using hash functions that distribute keys uniformly across buckets.",
    topic: "Hash Table",
    difficulty: "Easy"
  },
  {
    id: 2,
    question: "Which of the following data structures is most optimal for implementing a LIFO (Last-In-First-Out) access pattern?",
    options: [
      { key: "A", text: "Queue" },
      { key: "B", text: "Stack" },
      { key: "C", text: "Min Heap" },
      { key: "D", text: "Binary Search Tree" }
    ],
    correct_answer: "B",
    explanation: "A Stack provides LIFO semantics with O(1) push and pop operations at the top of the stack.",
    topic: "Stack",
    difficulty: "Easy"
  },
  {
    id: 3,
    question: "In Dijkstra's algorithm implemented with a Min-Heap (Priority Queue), what is the overall time complexity for a graph with V vertices and E edges?",
    options: [
      { key: "A", text: "O(V + E)" },
      { key: "B", text: "O(V²)" },
      { key: "C", text: "O((V + E) log V)" },
      { key: "D", text: "O(E log E)" }
    ],
    correct_answer: "C",
    explanation: "With an adjacency list and binary min-heap priority queue, extracting the minimum takes O(V log V) and updating edge weights takes O(E log V), yielding O((V + E) log V).",
    topic: "Graphs",
    difficulty: "Medium"
  },
  {
    id: 4,
    question: "What is the worst-case time complexity of QuickSort?",
    options: [
      { key: "A", text: "O(n log n)" },
      { key: "B", text: "O(n²)" },
      { key: "C", text: "O(n)" },
      { key: "D", text: "O(log n)" }
    ],
    correct_answer: "B",
    explanation: "QuickSort degrades to O(n²) when the chosen pivot is always the smallest or largest element (e.g., sorted array without randomized pivot).",
    topic: "Sorting & Searching",
    difficulty: "Easy"
  },
  {
    id: 5,
    question: "Which algorithmic paradigm does Floyd-Warshall algorithm for all-pairs shortest paths belong to?",
    options: [
      { key: "A", text: "Greedy Strategy" },
      { key: "B", text: "Divide and Conquer" },
      { key: "C", text: "Dynamic Programming" },
      { key: "D", text: "Backtracking" }
    ],
    correct_answer: "C",
    explanation: "Floyd-Warshall constructs solutions incrementally by considering each vertex as an intermediate point using a DP recurrence matrix.",
    topic: "Dynamic Programming",
    difficulty: "Hard"
  }
]

// ==========================================
// 2. SUB-COMPONENT: MCQOption
// ==========================================
function MCQOption({
  optionKey,
  optionText,
  isSelected,
  onSelect,
  isSubmitted,
  isCorrect,
  disabled
}) {
  let containerStyles = 'border-slate-200 hover:border-blue-300 hover:bg-blue-50/40 bg-white text-slate-800'
  let indicatorStyles = 'border-slate-300 text-slate-500'

  if (isSubmitted) {
    if (isCorrect) {
      containerStyles = 'border-emerald-500 bg-emerald-50/70 text-emerald-900 font-medium'
      indicatorStyles = 'border-emerald-500 bg-emerald-500 text-white'
    } else if (isSelected && !isCorrect) {
      containerStyles = 'border-rose-500 bg-rose-50/70 text-rose-900 font-medium'
      indicatorStyles = 'border-rose-500 bg-rose-500 text-white'
    } else {
      containerStyles = 'border-slate-200 bg-slate-50/40 text-slate-400 opacity-70'
      indicatorStyles = 'border-slate-200 text-slate-400'
    }
  } else if (isSelected) {
    containerStyles = 'border-blue-600 bg-blue-50/70 text-blue-900 font-medium ring-2 ring-blue-500/20'
    indicatorStyles = 'border-blue-600 bg-blue-600 text-white'
  }

  return (
    <button
      type="button"
      disabled={disabled || isSubmitted}
      onClick={() => onSelect(optionKey)}
      className={`w-full text-left p-4 rounded-xl border transition-all flex items-center justify-between gap-4 ${containerStyles} ${
        !isSubmitted && !disabled ? 'cursor-pointer' : 'cursor-default'
      }`}
    >
      <div className="flex items-center gap-3.5">
        <span
          className={`w-7 h-7 rounded-lg border text-xs font-bold flex items-center justify-center shrink-0 transition-colors ${indicatorStyles}`}
        >
          {optionKey}
        </span>
        <span className="text-sm font-mono leading-relaxed">{optionText}</span>
      </div>

      {isSubmitted && (
        <div className="shrink-0">
          {isCorrect && <CheckCircle2 className="w-5 h-5 text-emerald-600" />}
          {isSelected && !isCorrect && <XCircle className="w-5 h-5 text-rose-600" />}
        </div>
      )}
    </button>
  )
}

// ==========================================
// 3. SUB-COMPONENT: MCQCard
// ==========================================
function MCQCard({
  questionData,
  currentQuestionIndex,
  totalQuestions,
  selectedAnswer,
  onSelectAnswer,
  isSubmitted,
  onSubmitAnswer,
  onNextQuestion,
  isLastQuestion
}) {
  const { question, options, correct_answer, explanation, topic, difficulty } = questionData

  return (
    <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm">
      {/* Top Question Meta */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-slate-100">
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-blue-600 bg-blue-50 border border-blue-100 px-3 py-1 rounded-full">
            Question {currentQuestionIndex + 1} / {totalQuestions}
          </span>
          <span className="text-xs font-semibold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-full">
            {topic}
          </span>
        </div>

        <span
          className={`text-xs font-bold px-2.5 py-1 rounded-md ${
            difficulty === 'Easy'
              ? 'bg-emerald-50 text-emerald-700'
              : difficulty === 'Medium'
              ? 'bg-amber-50 text-amber-700'
              : 'bg-rose-50 text-rose-700'
          }`}
        >
          {difficulty}
        </span>
      </div>

      {/* Main Question Text */}
      <div className="py-6">
        <h2 className="text-lg sm:text-xl font-bold text-slate-900 leading-snug">
          {question}
        </h2>
      </div>

      {/* Options List */}
      <div className="space-y-3 mb-6">
        {options.map((opt) => (
          <MCQOption
            key={opt.key}
            optionKey={opt.key}
            optionText={opt.text}
            isSelected={selectedAnswer === opt.key}
            onSelect={onSelectAnswer}
            isSubmitted={isSubmitted}
            isCorrect={opt.key === correct_answer}
            disabled={isSubmitted}
          />
        ))}
      </div>

      {/* Post-Submission Explanation Box */}
      {isSubmitted && (
        <div className="mb-6 p-4 sm:p-5 rounded-xl border border-blue-100 bg-blue-50/50 text-slate-800 transition-all">
          <div className="flex items-center gap-2 text-xs font-bold text-blue-700 uppercase tracking-wider mb-2">
            <Sparkles className="w-4 h-4 text-blue-600" />
            <span>Explanation & Concept Breakdown</span>
          </div>
          <p className="text-sm text-slate-700 leading-relaxed font-normal">
            {explanation}
          </p>
          <div className="mt-3 pt-3 border-t border-blue-200/60 flex items-center gap-2 text-xs font-medium text-blue-900">
            <span>Correct Answer:</span>
            <span className="font-bold px-2 py-0.5 rounded bg-blue-100/80 text-blue-800">
              Option {correct_answer}
            </span>
          </div>
        </div>
      )}

      {/* Footer Controls */}
      <div className="flex items-center justify-between pt-4 border-t border-slate-100">
        <div className="text-xs text-slate-400 flex items-center gap-1.5">
          <HelpCircle size={14} />
          <span>{isSubmitted ? 'Review explanation before proceeding' : 'Select an option to enable submission'}</span>
        </div>

        <div>
          {!isSubmitted ? (
            <button
              type="button"
              disabled={!selectedAnswer}
              onClick={onSubmitAnswer}
              className={`inline-flex items-center gap-2 px-6 py-2.5 rounded-xl text-sm font-semibold shadow-sm transition-all ${
                selectedAnswer
                  ? 'bg-blue-600 hover:bg-blue-700 text-white cursor-pointer active:scale-95'
                  : 'bg-slate-100 text-slate-400 cursor-not-allowed'
              }`}
            >
              <Check size={16} />
              Submit
            </button>
          ) : (
            <button
              type="button"
              onClick={onNextQuestion}
              className="inline-flex items-center gap-2 px-6 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-sm font-semibold shadow-sm transition-all active:scale-95 cursor-pointer"
            >
              <span>{isLastQuestion ? 'View Results' : 'Next Question'}</span>
              <ArrowRight size={16} />
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

// ==========================================
// 4. SUB-COMPONENT: MCQResult
// ==========================================
function MCQResult({
  score,
  totalQuestions,
  totalTimeSpent,
  onRestart,
  resultsList
}) {
  const percentage = Math.round((score / totalQuestions) * 100)
  const isPassed = percentage >= 60

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}m ${secs < 10 ? '0' : ''}${secs}s`
  }

  return (
    <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-10 shadow-sm max-w-2xl mx-auto text-center">
      <div
        className={`w-16 h-16 rounded-2xl mx-auto flex items-center justify-center mb-5 ${
          isPassed ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-600'
        }`}
      >
        <Award size={32} />
      </div>

      <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900">
        {isPassed ? 'Assessment Completed!' : 'Keep Practicing!'}
      </h1>
      <p className="mt-2 text-sm text-slate-500">
        Here is your performance breakdown for this MCQ test session.
      </p>

      {/* Main Score Box */}
      <div className="my-8 p-6 rounded-2xl bg-[#F8FAFC] border border-slate-200/80 grid grid-cols-3 gap-4 text-center">
        <div>
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Score</span>
          <p className="text-2xl sm:text-3xl font-black text-slate-900 mt-1">
            {score} <span className="text-sm font-medium text-slate-400">/ {totalQuestions}</span>
          </p>
        </div>
        <div>
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Accuracy</span>
          <p className={`text-2xl sm:text-3xl font-black mt-1 ${isPassed ? 'text-emerald-600' : 'text-amber-600'}`}>
            {percentage}%
          </p>
        </div>
        <div>
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Time Taken</span>
          <p className="text-lg sm:text-xl font-bold text-slate-800 mt-1.5 flex items-center justify-center gap-1">
            <Clock size={16} className="text-slate-400" />
            {formatTime(totalTimeSpent)}
          </p>
        </div>
      </div>

      {/* Question Summary */}
      <div className="text-left mb-8">
        <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">
          Question Summary ({resultsList.length})
        </h3>
        <div className="max-h-60 overflow-y-auto space-y-2 pr-1 divide-y divide-slate-100">
          {resultsList.map((res, idx) => (
            <div key={idx} className="pt-2 flex items-center justify-between text-xs">
              <span className="text-slate-700 truncate max-w-[70%]">
                {idx + 1}. {res.question}
              </span>
              <span
                className={`inline-flex items-center gap-1 px-2 py-0.5 rounded font-semibold ${
                  res.isCorrect ? 'bg-emerald-50 text-emerald-700' : 'bg-rose-50 text-rose-700'
                }`}
              >
                {res.isCorrect ? (
                  <>
                    <CheckCircle2 size={12} /> Correct
                  </>
                ) : (
                  <>
                    <XCircle size={12} /> Incorrect
                  </>
                )}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
        <button
          type="button"
          onClick={onRestart}
          className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl border border-slate-200 text-sm font-semibold text-slate-700 hover:bg-slate-50 transition-colors cursor-pointer"
        >
          <RotateCcw size={16} />
          Retake Test
        </button>
        <Link
          to="/practice"
          className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold shadow transition-all"
        >
          <span>Continue Practice</span>
          <ArrowRight size={16} />
        </Link>
      </div>
    </div>
  )
}

// ==========================================
// 5. MAIN PAGE: MCQ
// ==========================================
export default function MCQ() {
  const [questions] = useState(MCQ_DATABASE)
  const [currentIndex, setCurrentIndex] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState(null)
  const [isSubmitted, setIsSubmitted] = useState(false)
  const [score, setScore] = useState(0)
  const [resultsList, setResultsList] = useState([])
  const [isCompleted, setIsCompleted] = useState(false)

  // Timer: 15 minutes
  const [timerEnabled] = useState(true)
  const [timeRemaining, setTimeRemaining] = useState(15 * 60)
  const [totalTimeSpent, setTotalTimeSpent] = useState(0)

  const currentQuestion = questions[currentIndex]
  const totalQuestions = questions.length

  useEffect(() => {
    if (!timerEnabled || isCompleted) return

    const interval = setInterval(() => {
      setTimeRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(interval)
          setIsCompleted(true)
          return 0
        }
        return prev - 1
      })
      setTotalTimeSpent((prev) => prev + 1)
    }, 1000)

    return () => clearInterval(interval)
  }, [timerEnabled, isCompleted])

  const handleSelectAnswer = (optionKey) => {
    if (isSubmitted) return
    setSelectedAnswer(optionKey)
  }

  const handleSubmitAnswer = () => {
    if (!selectedAnswer || isSubmitted) return

    const isCorrect = selectedAnswer === currentQuestion.correct_answer
    if (isCorrect) {
      setScore((prev) => prev + 1)
    }

    setResultsList((prev) => [
      ...prev,
      {
        questionId: currentQuestion.id,
        question: currentQuestion.question,
        selectedAnswer,
        correctAnswer: currentQuestion.correct_answer,
        isCorrect
      }
    ])

    setIsSubmitted(true)
  }

  const handleNextQuestion = () => {
    if (currentIndex + 1 < totalQuestions) {
      setCurrentIndex((prev) => prev + 1)
      setSelectedAnswer(null)
      setIsSubmitted(false)
    } else {
      setIsCompleted(true)
    }
  }

  const handleRestart = () => {
    setCurrentIndex(0)
    setSelectedAnswer(null)
    setIsSubmitted(false)
    setScore(0)
    setResultsList([])
    setIsCompleted(false)
    setTimeRemaining(15 * 60)
    setTotalTimeSpent(0)
  }

  const formatTimer = (seconds) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`
  }

  return (
    <div className="max-w-[1100px] mx-auto pb-12">
      {/* Top Header Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-6">
        <Link
          to="/practice"
          className="inline-flex items-center gap-2 text-sm font-medium text-slate-500 hover:text-slate-900 transition-colors"
        >
          <ArrowLeft size={16} />
          <span>Exit to Practice</span>
        </Link>

        {timerEnabled && !isCompleted && (
          <div
            className={`inline-flex items-center gap-2 px-3.5 py-1.5 rounded-xl border text-sm font-mono font-semibold ${
              timeRemaining < 120
                ? 'bg-rose-50 text-rose-700 border-rose-200 animate-pulse'
                : 'bg-white text-slate-700 border-slate-200'
            }`}
          >
            <Timer size={16} className={timeRemaining < 120 ? 'text-rose-600' : 'text-blue-600'} />
            <span>Time Left: {formatTimer(timeRemaining)}</span>
          </div>
        )}
      </div>

      {/* Progress Bar */}
      {!isCompleted && (
        <div className="mb-6">
          <div className="flex justify-between text-xs font-semibold text-slate-500 mb-2">
            <span>Progress: Question {currentIndex + 1} of {totalQuestions}</span>
            <span>{Math.round(((currentIndex + 1) / totalQuestions) * 100)}%</span>
          </div>
          <div className="h-2 w-full bg-slate-200/80 rounded-full overflow-hidden">
            <div
              className="h-full bg-blue-600 rounded-full transition-all duration-300"
              style={{ width: `${((currentIndex + 1) / totalQuestions) * 100}%` }}
            />
          </div>
        </div>
      )}

      {/* Active Question or Results View */}
      {!isCompleted ? (
        <MCQCard
          questionData={currentQuestion}
          currentQuestionIndex={currentIndex}
          totalQuestions={totalQuestions}
          selectedAnswer={selectedAnswer}
          onSelectAnswer={handleSelectAnswer}
          isSubmitted={isSubmitted}
          onSubmitAnswer={handleSubmitAnswer}
          onNextQuestion={handleNextQuestion}
          isLastQuestion={currentIndex === totalQuestions - 1}
        />
      ) : (
        <MCQResult
          score={score}
          totalQuestions={totalQuestions}
          totalTimeSpent={totalTimeSpent}
          onRestart={handleRestart}
          resultsList={resultsList}
        />
      )}
    </div>
  )
}