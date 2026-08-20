import { useMemo, useState } from 'react'

import {
  CheckCircle2,
  ChevronDown,
  ChevronRight,
  Circle,
  Lock
} from 'lucide-react'

import { Link } from 'react-router-dom'

import { a2zTopics } from '../../data/a2z'


function A2Z() {

  const [openTopic, setOpenTopic] = useState('basics')


  const totalProblems = useMemo(() => {
    return a2zTopics.reduce(
      (total, topic) => total + topic.total,
      0
    )
  }, [])


  const completedProblems = useMemo(() => {
    return a2zTopics.reduce(
      (total, topic) => total + topic.progress,
      0
    )
  }, [])


  const overallProgress =
    totalProblems === 0
      ? 0
      : Math.round(
          (completedProblems / totalProblems) * 100
        )


  const toggleTopic = (id) => {
    setOpenTopic(
      openTopic === id ? null : id
    )
  }


  return (
    <div className="max-w-7xl mx-auto pb-10 space-y-7">

      {/* HEADER */}

      <section>

        <p className="text-sm font-medium text-blue-600">
          A2Z DSA
        </p>

        <h1 className="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          Master DSA step by step
        </h1>

        <p className="mt-2 max-w-2xl text-slate-500">
          Follow a structured roadmap from the basics to advanced
          data structures and algorithms.
        </p>

      </section>


      {/* PROGRESS CARD */}

      <section className="bg-white border border-slate-200 rounded-2xl p-6">

        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

          <div>

            <p className="text-sm font-semibold text-slate-900">
              Your A2Z Progress
            </p>

            <p className="mt-1 text-xs text-slate-500">
              {completedProblems} of {totalProblems} problems completed
            </p>

          </div>

          <div className="text-2xl font-bold text-slate-900">
            {overallProgress}%
          </div>

        </div>


        <div className="mt-5 h-2.5 rounded-full bg-slate-100 overflow-hidden">

          <div
            className="h-full rounded-full bg-blue-600 transition-all"
            style={{
              width: `${overallProgress}%`
            }}
          />

        </div>

      </section>


      {/* ROADMAP */}

      <section>

        <div className="mb-4">

          <h2 className="text-xl font-semibold text-slate-900">
            A2Z Roadmap
          </h2>

          <p className="mt-1 text-sm text-slate-500">
            Complete each section to build your DSA foundation.
          </p>

        </div>


        <div className="space-y-3">

          {a2zTopics.map((topic) => {

            const isOpen = openTopic === topic.id

            const topicProgress =
              topic.total === 0
                ? 0
                : Math.round(
                    (topic.progress / topic.total) * 100
                  )


            return (
              <div
                key={topic.id}
                className="bg-white border border-slate-200 rounded-2xl overflow-hidden"
              >

                {/* TOPIC HEADER */}

                <button
                  type="button"
                  onClick={() => toggleTopic(topic.id)}
                  className="w-full px-5 py-5 flex items-center gap-4 text-left hover:bg-slate-50 transition"
                >

                  {/* NUMBER */}

                  <div className="w-10 h-10 rounded-xl bg-slate-100 flex items-center justify-center shrink-0">

                    <span className="text-xs font-bold text-slate-500">
                      {topic.number}
                    </span>

                  </div>


                  {/* INFO */}

                  <div className="flex-1 min-w-0">

                    <div className="flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-3">

                      <h3 className="font-semibold text-slate-900">
                        {topic.title}
                      </h3>

                      <span className="text-xs text-slate-400">
                        {topic.progress}/{topic.total} completed
                      </span>

                    </div>

                    <p className="mt-1 text-xs text-slate-500">
                      {topic.description}
                    </p>


                    {/* PROGRESS */}

                    <div className="mt-3 flex items-center gap-3">

                      <div className="h-1.5 flex-1 max-w-xs rounded-full bg-slate-100 overflow-hidden">

                        <div
                          className="h-full rounded-full bg-blue-500"
                          style={{
                            width: `${topicProgress}%`
                          }}
                        />

                      </div>

                      <span className="text-[11px] text-slate-400">
                        {topicProgress}%
                      </span>

                    </div>

                  </div>


                  {/* ICON */}

                  <div className="text-slate-400">

                    {isOpen ? (
                      <ChevronDown size={19} />
                    ) : (
                      <ChevronRight size={19} />
                    )}

                  </div>

                </button>


                {/* PROBLEMS */}

                {isOpen && (

                  <div className="border-t border-slate-100">

                    {topic.problems.length > 0 ? (

                      topic.problems.map((problem) => (

                        <Link
                          key={problem.problemId}
                          to={`/problem/${problem.problemId}`}
                          className="flex items-center gap-3 px-5 py-4 pl-20 hover:bg-slate-50 transition border-b border-slate-50 last:border-b-0"
                        >

                          <Circle
                            size={17}
                            className="text-slate-300 shrink-0"
                          />

                          <div className="flex-1">

                            <p className="text-sm font-medium text-slate-800">
                              {problem.title}
                            </p>

                            <p className="mt-0.5 text-[11px] text-slate-400">
                              {problem.difficulty}
                            </p>

                          </div>

                          <ChevronRight
                            size={16}
                            className="text-slate-300"
                          />

                        </Link>

                      ))

                    ) : (

                      <div className="px-5 py-8 text-center">

                        <Lock
                          size={20}
                          className="mx-auto text-slate-300"
                        />

                        <p className="mt-2 text-xs font-medium text-slate-500">
                          Problems coming soon
                        </p>

                        <p className="mt-1 text-[11px] text-slate-400">
                          This section will be connected to the DSA problem library.
                        </p>

                      </div>

                    )}

                  </div>

                )}

              </div>
            )
          })}

        </div>

      </section>

    </div>
  )
}


export default A2Z