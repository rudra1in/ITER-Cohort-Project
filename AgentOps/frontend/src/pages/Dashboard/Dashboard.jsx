import {
  ArrowRight,
  Flame,
  Target,
  Trophy,
  Brain,
  Code2
} from 'lucide-react'
import { Link } from 'react-router-dom'

const stats = [
  {
    label: 'Problems Solved',
    value: '24',
    description: '+4 this week',
    icon: Trophy
  },
  {
    label: 'Current Streak',
    value: '7 days',
    description: 'Keep it going',
    icon: Flame
  },
  {
    label: 'Overall Progress',
    value: '42%',
    description: '12 of 28 topics',
    icon: Target
  },
  {
    label: 'Accuracy',
    value: '78%',
    description: '+6% this month',
    icon: Brain
  }
]

function Dashboard() {
  return (
    <div className="max-w-7xl mx-auto space-y-8">

      {/* Header */}
      <section>
        <p className="text-sm font-medium text-blue-600">
          Your learning workspace
        </p>

        <h1 className="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          Good evening, Isha 👋
        </h1>

        <p className="mt-2 text-slate-500">
          Keep building your problem-solving skills, one problem at a time.
        </p>
      </section>


      {/* Stats */}
      <section className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4">

        {stats.map((stat) => {
          const Icon = stat.icon

          return (
            <div
              key={stat.label}
              className="bg-white border border-slate-200 rounded-2xl p-5 hover:border-slate-300 transition-colors"
            >

              <div className="flex items-start justify-between">

                <div>
                  <p className="text-sm text-slate-500">
                    {stat.label}
                  </p>

                  <p className="mt-2 text-2xl font-bold text-slate-900">
                    {stat.value}
                  </p>
                </div>

                <div className="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
                  <Icon size={19} />
                </div>

              </div>

              <p className="mt-3 text-xs text-slate-400">
                {stat.description}
              </p>

            </div>
          )
        })}

      </section>


      {/* Main learning area */}
      <section className="grid grid-cols-1 xl:grid-cols-3 gap-6">

        {/* Continue learning */}
        <div className="xl:col-span-2 bg-white border border-slate-200 rounded-2xl p-6">

          <div className="flex items-start justify-between">

            <div>
              <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                Continue Learning
              </p>

              <h2 className="mt-2 text-xl font-semibold text-slate-900">
                Arrays & Hashing
              </h2>

              <p className="mt-1 text-sm text-slate-500">
                Build your foundation with common array and hash map patterns.
              </p>
            </div>

            <div className="hidden sm:flex w-11 h-11 rounded-xl bg-slate-100 items-center justify-center text-slate-600">
              <Code2 size={20} />
            </div>

          </div>


          {/* Progress */}
          <div className="mt-6">

            <div className="flex items-center justify-between mb-2">

              <span className="text-sm font-medium text-slate-700">
                Topic progress
              </span>

              <span className="text-sm font-semibold text-slate-900">
                72%
              </span>

            </div>

            <div className="h-2 bg-slate-100 rounded-full overflow-hidden">

              <div
                className="h-full bg-blue-600 rounded-full"
                style={{ width: '72%' }}
              />

            </div>

          </div>


          <div className="mt-6 flex items-center justify-between">

            <p className="text-sm text-slate-500">
              8 of 11 problems completed
            </p>

            <Link
              to="/practice"
              className="inline-flex items-center gap-2 text-sm font-semibold text-blue-600 hover:text-blue-700"
            >
              Continue Practice
              <ArrowRight size={16} />
            </Link>

          </div>

        </div>


        {/* AI Coach */}
        <div className="bg-slate-900 text-white rounded-2xl p-6">

          <div className="w-11 h-11 rounded-xl bg-white/10 flex items-center justify-center">
            <Brain size={21} />
          </div>

          <p className="mt-5 text-xs font-semibold uppercase tracking-wider text-slate-400">
            AI Coach
          </p>

          <h2 className="mt-2 text-xl font-semibold">
            Stuck on a problem?
          </h2>

          <p className="mt-2 text-sm leading-relaxed text-slate-400">
            Get progressive hints, understand your mistakes, and learn the
            reasoning behind a solution.
          </p>

          <Link
            to="/ai-coach"
            className="mt-6 inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white text-slate-900 text-sm font-semibold hover:bg-slate-100 transition-colors"
          >
            Open AI Coach
            <ArrowRight size={16} />
          </Link>

        </div>

      </section>


      {/* Today's challenge */}
      <section>

        <div className="flex items-center justify-between mb-4">

          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
              Daily Practice
            </p>

            <h2 className="mt-1 text-xl font-semibold text-slate-900">
              Today's Challenge
            </h2>
          </div>

          <Link
            to="/practice"
            className="text-sm font-medium text-slate-500 hover:text-slate-900"
          >
            View all
          </Link>

        </div>


        <div className="bg-white border border-slate-200 rounded-2xl p-6">

          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">

            <div className="flex items-start gap-4">

              <div className="w-11 h-11 shrink-0 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
                <Code2 size={20} />
              </div>

              <div>

                <div className="flex flex-wrap items-center gap-2">

                  <h3 className="font-semibold text-slate-900">
                    Two Sum
                  </h3>

                  <span className="px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 text-xs font-medium">
                    Easy
                  </span>

                </div>

                <p className="mt-1 text-sm text-slate-500">
                  Arrays · Hash Map
                </p>

                <p className="mt-3 text-sm text-slate-600">
                  Find two numbers in an array that add up to a target value.
                </p>

              </div>

            </div>


            <Link
              to="/problem/two-sum"
              className="inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-blue-600 text-white text-sm font-semibold hover:bg-blue-700 transition-colors"
            >
              Start Problem
              <ArrowRight size={16} />
            </Link>

          </div>

        </div>

      </section>

    </div>
  )
}

export default Dashboard