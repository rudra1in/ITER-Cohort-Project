import { useMemo, useState } from 'react'

import {
  Search,
  SlidersHorizontal,
  ArrowRight,
  CheckCircle2,
  Circle
} from 'lucide-react'

import { Link } from 'react-router-dom'

import { problems } from '../../data/problem'


function Practice() {

  const [search, setSearch] = useState('')
  const [difficulty, setDifficulty] = useState('All')
  const [topic, setTopic] = useState('All')


  // Get topics dynamically from the problem data
  const topics = [
    'All',
    ...new Set(
      problems.map((problem) => problem.topic)
    )
  ]


  // Filter problems
  const filteredProblems = useMemo(() => {

    return problems.filter((problem) => {

      const searchText = search
        .toLowerCase()
        .trim()


      const matchesSearch =
        problem.title
          .toLowerCase()
          .includes(searchText) ||

        problem.topic
          .toLowerCase()
          .includes(searchText) ||

        problem.pattern
          .toLowerCase()
          .includes(searchText)


      const matchesDifficulty =
        difficulty === 'All' ||
        problem.difficulty === difficulty


      const matchesTopic =
        topic === 'All' ||
        problem.topic === topic


      return (
        matchesSearch &&
        matchesDifficulty &&
        matchesTopic
      )

    })

  }, [search, difficulty, topic])


  return (

    <div className="max-w-7xl mx-auto space-y-7">

      {/* ================================================= */}
      {/* HEADER */}
      {/* ================================================= */}

      <section>

        <p className="text-sm font-medium text-blue-600">
          Practice
        </p>


        <h1 className="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          Build your problem-solving skills
        </h1>


        <p className="mt-2 text-slate-500">
          Practice problems, recognize patterns, and strengthen your DSA
          fundamentals.
        </p>

      </section>


      {/* ================================================= */}
      {/* SEARCH & FILTERS */}
      {/* ================================================= */}

      <section className="bg-white border border-slate-200 rounded-2xl p-4">

        <div className="flex flex-col lg:flex-row gap-3">


          {/* Search */}

          <div className="relative flex-1">

            <Search
              size={18}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
            />


            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search problems..."
              className="
                w-full h-11
                pl-10 pr-4
                rounded-xl
                border border-slate-200
                bg-slate-50
                text-sm
                outline-none
                focus:bg-white
                focus:border-blue-400
                focus:ring-2
                focus:ring-blue-100
              "
            />

          </div>


          {/* Difficulty */}

          <select
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            className="
              h-11 px-4
              rounded-xl
              border border-slate-200
              bg-slate-50
              text-sm
              text-slate-600
              outline-none
              focus:bg-white
              focus:border-blue-400
            "
          >

            <option value="All">
              All difficulties
            </option>

            <option value="Easy">
              Easy
            </option>

            <option value="Medium">
              Medium
            </option>

            <option value="Hard">
              Hard
            </option>

          </select>


          {/* Topic */}

          <select
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            className="
              h-11 px-4
              rounded-xl
              border border-slate-200
              bg-slate-50
              text-sm
              text-slate-600
              outline-none
              focus:bg-white
              focus:border-blue-400
            "
          >

            {topics.map((item) => (

              <option
                key={item}
                value={item}
              >
                {item === 'All'
                  ? 'All topics'
                  : item}
              </option>

            ))}

          </select>


          {/* Filters button */}

          <button
            type="button"
            className="
              h-11 px-4
              rounded-xl
              border border-slate-200
              text-slate-600
              hover:bg-slate-50
              transition-colors
              flex items-center
              justify-center
              gap-2
            "
          >

            <SlidersHorizontal size={17} />

            Filters

          </button>

        </div>

      </section>


      {/* ================================================= */}
      {/* PRACTICE SUMMARY */}
      {/* ================================================= */}

      <section className="grid grid-cols-1 sm:grid-cols-3 gap-4">


        {/* Total */}

        <div className="bg-white border border-slate-200 rounded-2xl p-5">

          <p className="text-sm text-slate-500">
            Total Problems
          </p>


          <p className="mt-2 text-2xl font-bold text-slate-900">
            {problems.length}
          </p>

        </div>


        {/* Completed */}

        <div className="bg-white border border-slate-200 rounded-2xl p-5">

          <p className="text-sm text-slate-500">
            Completed
          </p>


          <p className="mt-2 text-2xl font-bold text-slate-900">

            {
              problems.filter(
                (problem) => problem.solved
              ).length
            }

          </p>

        </div>


        {/* Remaining */}

        <div className="bg-white border border-slate-200 rounded-2xl p-5">

          <p className="text-sm text-slate-500">
            Remaining
          </p>


          <p className="mt-2 text-2xl font-bold text-slate-900">

            {
              problems.filter(
                (problem) => !problem.solved
              ).length
            }

          </p>

        </div>

      </section>


      {/* ================================================= */}
      {/* PROBLEM LIST */}
      {/* ================================================= */}

      <section>


        {/* Problem list header */}

        <div className="flex items-center justify-between mb-4">

          <div>

            <h2 className="text-xl font-semibold text-slate-900">
              Problems
            </h2>


            <p className="mt-1 text-sm text-slate-500">
              Start with the problems recommended for your current level.
            </p>

          </div>


          <span className="text-sm text-slate-400">
            {filteredProblems.length} shown
          </span>

        </div>


        {/* ================================================= */}
        {/* RESULTS */}
        {/* ================================================= */}

        {filteredProblems.length > 0 ? (

          <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden">

            {filteredProblems.map(
              (problem, index) => (

                <div
                  key={problem.id}
                  className={`
                    p-5
                    flex
                    flex-col
                    lg:flex-row
                    lg:items-center
                    justify-between
                    gap-4
                    hover:bg-slate-50
                    transition-colors
                    ${
                      index !== filteredProblems.length - 1
                        ? 'border-b border-slate-100'
                        : ''
                    }
                  `}
                >


                  {/* Left side */}

                  <div className="flex items-start gap-4">


                    {/* Status */}

                    <div className="mt-1">

                      {problem.solved ? (

                        <CheckCircle2
                          size={20}
                          className="text-emerald-500"
                        />

                      ) : (

                        <Circle
                          size={20}
                          className="text-slate-300"
                        />

                      )}

                    </div>


                    {/* Problem information */}

                    <div>

                      <h3 className="font-semibold text-slate-900">
                        {problem.title}
                      </h3>


                      <div className="mt-2 flex flex-wrap items-center gap-2">


                        {/* Difficulty */}

                        <span
                          className={`
                            px-2
                            py-0.5
                            rounded-md
                            text-xs
                            font-medium

                            ${
                              problem.difficulty === 'Easy'
                                ? 'bg-emerald-50 text-emerald-700'

                                : problem.difficulty === 'Medium'
                                  ? 'bg-amber-50 text-amber-700'

                                  : 'bg-red-50 text-red-700'
                            }
                          `}
                        >
                          {problem.difficulty}
                        </span>


                        {/* Topic */}

                        <span className="text-xs text-slate-400">
                          {problem.topic}
                        </span>


                        <span className="text-slate-300">
                          •
                        </span>


                        {/* Pattern */}

                        <span className="text-xs text-slate-400">
                          {problem.pattern}
                        </span>

                      </div>

                    </div>

                  </div>


                  {/* Solve / Review */}

                  <Link
                    to={`/problem/${problem.id}`}
                    className="
                      inline-flex
                      items-center
                      justify-center
                      gap-2
                      px-4
                      py-2.5
                      rounded-xl
                      text-sm
                      font-semibold
                      text-blue-600
                      hover:bg-blue-50
                      transition-colors
                    "
                  >

                    {problem.solved
                      ? 'Review'
                      : 'Solve'
                    }

                    <ArrowRight size={16} />

                  </Link>

                </div>

              )
            )}

          </div>

        ) : (

          /* ================================================= */
          /* EMPTY STATE */
          /* ================================================= */

          <div className="bg-white border border-slate-200 rounded-2xl py-16 text-center">

            <Search
              size={28}
              className="mx-auto text-slate-300"
            />


            <h3 className="mt-3 text-sm font-semibold text-slate-800">
              No problems found
            </h3>


            <p className="mt-1 text-xs text-slate-500">
              Try changing your search or filters.
            </p>

          </div>

        )}

      </section>

    </div>

  )
}


export default Practice