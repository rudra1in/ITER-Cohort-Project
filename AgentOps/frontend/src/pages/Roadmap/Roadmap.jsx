import {
  ArrowRight,
  CheckCircle2,
  Lock,
  Play,
  Sparkles,
  Target,
  Trophy
} from 'lucide-react'

import { Link } from 'react-router-dom'

import { roadmap } from '../../data/roadmap'


function getProgress(completed, total) {
  if (!total) return 0

  return Math.round((completed / total) * 100)
}


function Roadmap() {

  const totalProblems = roadmap.reduce(
    (sum, section) => sum + section.problems,
    0
  )

  const completedProblems = roadmap.reduce(
    (sum, section) =>
      sum +
      Math.round((section.progress / 100) * section.problems),
    0
  )

  const overallProgress = getProgress(
    completedProblems,
    totalProblems
  )

  const currentTopic = roadmap.find(
    (section) =>
      section.status === 'current' ||
      section.status === 'unlocked'
  )


  return (
    <div className="max-w-7xl mx-auto space-y-8 pb-10">

      {/* ========================================= */}
      {/* HEADER */}
      {/* ========================================= */}

      <section>

        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6">

          <div>

            <div className="flex items-center gap-2 text-sm font-medium text-blue-600">

              <Target size={16} />

              Your DSA Roadmap

            </div>


            <h1 className="mt-2 text-3xl lg:text-4xl font-bold tracking-tight text-slate-900">

              Build your DSA skills,

              <span className="text-blue-600">
                {' '}step by step.
              </span>

            </h1>


            <p className="mt-3 max-w-2xl text-slate-500 leading-7">

              Follow a structured learning path from fundamentals
              to advanced problem-solving. Build concepts first,
              then strengthen them through practice.

            </p>

          </div>


          <Link
            to="/practice"
            className="
              inline-flex
              items-center
              justify-center
              gap-2
              px-4
              py-2.5
              rounded-xl
              bg-slate-900
              text-white
              text-sm
              font-semibold
              hover:bg-slate-800
              transition
              shadow-sm
            "
          >

            Practice Problems

            <ArrowRight size={16} />

          </Link>

        </div>

      </section>


      {/* ========================================= */}
      {/* PROGRESS OVERVIEW */}
      {/* ========================================= */}

      <section
        className="
          relative
          overflow-hidden
          rounded-2xl
          border
          border-slate-200
          bg-white
          shadow-sm
        "
      >

        <div
          className="
            absolute
            -right-20
            -top-20
            h-56
            w-56
            rounded-full
            bg-blue-50
            blur-3xl
          "
        />


        <div className="relative p-6 lg:p-7">

          <div className="flex flex-col lg:flex-row lg:items-center gap-7">

            {/* Progress circle */}

            <div className="relative w-28 h-28 shrink-0">

              <svg
                viewBox="0 0 120 120"
                className="w-full h-full -rotate-90"
              >

                <circle
                  cx="60"
                  cy="60"
                  r="48"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="9"
                  className="text-slate-100"
                />

                <circle
                  cx="60"
                  cy="60"
                  r="48"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="9"
                  strokeLinecap="round"
                  strokeDasharray={`${overallProgress * 3.02} 302`}
                  className="text-blue-600"
                />

              </svg>


              <div className="absolute inset-0 flex flex-col items-center justify-center">

                <span className="text-xl font-bold text-slate-900">
                  {overallProgress}%
                </span>

                <span className="text-[10px] text-slate-400">
                  complete
                </span>

              </div>

            </div>


            {/* Progress information */}

            <div className="flex-1">

              <div className="flex flex-wrap items-center gap-2">

                <span className="px-2.5 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-semibold">
                  Current focus
                </span>

                <span className="text-xs text-slate-400">
                  Keep building momentum
                </span>

              </div>


              <h2 className="mt-3 text-xl font-bold text-slate-900">

                {currentTopic?.title || 'Start your journey'}

              </h2>


              <p className="mt-1 text-sm text-slate-500">

                {currentTopic?.description ||
                  'Begin with the fundamentals and build your DSA foundation.'}

              </p>


              <div className="mt-5 max-w-xl">

                <div className="flex items-center justify-between text-xs">

                  <span className="font-medium text-slate-500">
                    Overall progress
                  </span>

                  <span className="font-semibold text-slate-700">
                    {completedProblems} / {totalProblems} problems
                  </span>

                </div>


                <div className="mt-2 h-2 rounded-full bg-slate-100 overflow-hidden">

                  <div
                    className="h-full rounded-full bg-blue-600 transition-all duration-500"
                    style={{
                      width: `${overallProgress}%`
                    }}
                  />

                </div>

              </div>

            </div>


            {/* Continue */}

            {currentTopic && (

              <Link
                to="/practice"
                className="
                  shrink-0
                  inline-flex
                  items-center
                  justify-center
                  gap-2
                  px-4
                  py-2.5
                  rounded-xl
                  border
                  border-slate-200
                  bg-white
                  text-sm
                  font-semibold
                  text-slate-700
                  hover:border-blue-200
                  hover:text-blue-600
                  hover:bg-blue-50
                  transition
                "
              >

                <Play size={15} />

                Continue

              </Link>

            )}

          </div>

        </div>

      </section>


      {/* ========================================= */}
      {/* LEARNING PATH */}
      {/* ========================================= */}

      <section>

        <div className="flex items-center justify-between mb-5">

          <div>

            <h2 className="text-xl font-bold text-slate-900">
              Learning path
            </h2>

            <p className="mt-1 text-sm text-slate-500">
              Progress through each stage at your own pace.
            </p>

          </div>


          <div className="hidden sm:flex items-center gap-2 text-xs text-slate-400">

            <Sparkles size={14} />

            Structured for placements

          </div>

        </div>


        <div className="space-y-4">

          {roadmap.map((section, index) => {

            const isCompleted =
              section.status === 'completed'

            const isCurrent =
              section.status === 'current'

            const isUnlocked =
              section.status === 'unlocked'

            const isLocked =
              section.status === 'locked'


            return (

              <div
                key={section.id}
                className={`
                  group
                  relative
                  overflow-hidden
                  rounded-2xl
                  border
                  bg-white
                  shadow-sm
                  transition

                  ${
                    isCurrent
                      ? 'border-blue-200 shadow-blue-100/50'
                      : 'border-slate-200'
                  }

                  ${
                    isLocked
                      ? 'opacity-75'
                      : 'hover:border-slate-300 hover:shadow-md'
                  }
                `}
              >

                {/* Top section */}

                <div className="p-5 lg:p-6">

                  <div className="flex flex-col lg:flex-row lg:items-center gap-5">

                    {/* Number / status */}

                    <div
                      className={`
                        w-12
                        h-12
                        rounded-xl
                        flex
                        items-center
                        justify-center
                        shrink-0

                        ${
                          isCompleted
                            ? 'bg-emerald-50 text-emerald-600'
                            : isCurrent
                              ? 'bg-blue-50 text-blue-600'
                              : isUnlocked
                                ? 'bg-violet-50 text-violet-600'
                                : 'bg-slate-100 text-slate-400'
                        }
                      `}
                    >

                      {isCompleted ? (

                        <CheckCircle2 size={21} />

                      ) : isLocked ? (

                        <Lock size={18} />

                      ) : (

                        <span className="text-sm font-bold">
                          {String(index + 1).padStart(2, '0')}
                        </span>

                      )}

                    </div>


                    {/* Main info */}

                    <div className="flex-1 min-w-0">

                      <div className="flex flex-wrap items-center gap-2">

                        <h3 className="text-lg font-bold text-slate-900">
                          {section.title}
                        </h3>


                        <span
                          className={`
                            px-2
                            py-0.5
                            rounded-full
                            text-[10px]
                            font-semibold

                            ${
                              isCompleted
                                ? 'bg-emerald-50 text-emerald-700'
                                : isCurrent
                                  ? 'bg-blue-50 text-blue-700'
                                  : isUnlocked
                                    ? 'bg-violet-50 text-violet-700'
                                    : 'bg-slate-100 text-slate-500'
                            }
                          `}
                        >

                          {isCompleted
                            ? 'Completed'
                            : isCurrent
                              ? 'Current'
                              : isUnlocked
                                ? 'Unlocked'
                                : 'Locked'}

                        </span>

                      </div>


                      <p className="mt-1 text-sm text-slate-500">
                        {section.description}
                      </p>


                      <div className="mt-2 text-xs text-slate-400">
                        {section.level} · {section.problems} problems
                      </div>

                    </div>


                    {/* Progress */}

                    <div className="lg:w-44 shrink-0">

                      <div className="flex items-center justify-between text-xs">

                        <span className="text-slate-400">
                          Progress
                        </span>

                        <span className="font-semibold text-slate-700">
                          {section.progress}%
                        </span>

                      </div>


                      <div className="mt-2 h-1.5 rounded-full bg-slate-100 overflow-hidden">

                        <div
                          className={`
                            h-full
                            rounded-full
                            transition-all

                            ${
                              isCompleted
                                ? 'bg-emerald-500'
                                : isCurrent
                                  ? 'bg-blue-600'
                                  : 'bg-slate-300'
                            }
                          `}
                          style={{
                            width: `${section.progress}%`
                          }}
                        />

                      </div>

                    </div>

                  </div>

                </div>


                {/* Topics */}

                <div className="border-t border-slate-100">

                  <div className="px-5 lg:px-6 py-4">

                    <div className="flex flex-wrap gap-2">

                      {section.topics.map((topic) => (

                        <span
                          key={`${section.id}-${topic}`}
                          className={`
                            px-3
                            py-1.5
                            rounded-lg
                            text-xs
                            font-medium
                            border

                            ${
                              isLocked
                                ? 'bg-slate-50 border-slate-100 text-slate-400'
                                : isCompleted
                                  ? 'bg-emerald-50 border-emerald-100 text-emerald-700'
                                  : isCurrent
                                    ? 'bg-blue-50 border-blue-100 text-blue-700'
                                    : 'bg-slate-50 border-slate-200 text-slate-600'
                            }
                          `}
                        >

                          {topic}

                        </span>

                      ))}

                    </div>

                  </div>


                  {/* Action */}

                  {!isLocked && (

                    <div className="px-5 lg:px-6 pb-5">

                      <Link
                        to="/practice"
                        className="
                          inline-flex
                          items-center
                          gap-2
                          text-sm
                          font-semibold
                          text-blue-600
                          hover:text-blue-700
                        "
                      >

                        {isCompleted
                          ? 'Review problems'
                          : 'Continue learning'}

                        <ArrowRight
                          size={15}
                          className="group-hover:translate-x-0.5 transition"
                        />

                      </Link>

                    </div>

                  )}

                </div>

              </div>

            )

          })}

        </div>

      </section>


      {/* ========================================= */}
      {/* AI COACH */}
      {/* ========================================= */}

      <section
        className="
          relative
          overflow-hidden
          rounded-2xl
          bg-slate-900
          text-white
          shadow-sm
        "
      >

        <div
          className="
            absolute
            -right-16
            -top-24
            w-64
            h-64
            rounded-full
            bg-blue-500/10
            blur-3xl
          "
        />


        <div className="relative p-6 lg:p-7 flex flex-col md:flex-row md:items-center gap-6">

          <div className="w-11 h-11 rounded-xl bg-white/10 flex items-center justify-center shrink-0">

            <Sparkles
              size={20}
              className="text-blue-300"
            />

          </div>


          <div className="flex-1">

            <p className="text-xs font-semibold uppercase tracking-wider text-blue-300">
              AI Coach
            </p>


            <h2 className="mt-1 text-lg font-bold">
              Stuck on a problem?
            </h2>


            <p className="mt-1 text-sm leading-6 text-slate-400">
              Get a progressive hint, understand the pattern,
              and learn how to approach the problem without
              immediately revealing the solution.
            </p>

          </div>


          <Link
            to="/practice"
            className="
              inline-flex
              items-center
              justify-center
              gap-2
              px-4
              py-2.5
              rounded-xl
              bg-white
              text-slate-900
              text-sm
              font-semibold
              hover:bg-slate-100
              transition
              shrink-0
            "
          >

            Explore Problems

            <ArrowRight size={16} />

          </Link>

        </div>

      </section>


      {/* ========================================= */}
      {/* FOOTER MESSAGE */}
      {/* ========================================= */}

      <section className="flex items-center justify-center gap-2 text-xs text-slate-400">

        <Trophy size={14} />

        Consistency beats memorization. Keep solving.

      </section>

    </div>
  )
}


export default Roadmap