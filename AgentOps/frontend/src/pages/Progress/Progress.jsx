import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import {
  Flame,
  CheckCircle2,
  Target,
  Clock,
  TrendingUp,
  Cpu,
  Layers,
  ArrowUpRight,
  Filter,
  BarChart2
} from 'lucide-react'

// Demo initial state structured for standard API payload mapping
const INITIAL_PROGRESS_DATA = {
  stats: {
    problemsAttempted: 142,
    problemsSolved: 98,
    attemptCount: 310,
    successfulAttempts: 124,
    accuracy: 78.4,
    currentStreak: 12,
    bestStreak: 28,
  },
  difficultyBreakdown: {
    easy: { solved: 52, total: 80 },
    medium: { solved: 38, total: 120 },
    hard: { solved: 8, total: 40 }
  },
  topicProgress: [
    { topic: 'Arrays & Hashing', solved: 28, total: 35, percentage: 80 },
    { topic: 'Two Pointers', solved: 14, total: 20, percentage: 70 },
    { topic: 'Sliding Window', solved: 9, total: 15, percentage: 60 },
    { topic: 'Stack & Queue', solved: 12, total: 18, percentage: 66 },
    { topic: 'Binary Search', solved: 11, total: 16, percentage: 68 },
    { topic: 'Trees & Graphs', solved: 16, total: 30, percentage: 53 },
    { topic: 'Dynamic Programming', solved: 8, total: 25, percentage: 32 }
  ],
  recentAttempts: [
    {
      id: 'two-sum',
      title: 'Two Sum',
      topic: 'Arrays',
      difficulty: 'Easy',
      status: 'Accepted',
      lastAttempt: '2 hours ago',
      bestRuntime: '1 ms',
      bestMemory: '42.3 MB',
      attempts: 2
    },
    {
      id: '3sum',
      title: '3Sum',
      topic: 'Two Pointers',
      difficulty: 'Medium',
      status: 'Accepted',
      lastAttempt: '1 day ago',
      bestRuntime: '28 ms',
      bestMemory: '51.2 MB',
      attempts: 4
    },
    {
      id: 'trapping-rain-water',
      title: 'Trapping Rain Water',
      topic: 'Two Pointers',
      difficulty: 'Hard',
      status: 'Wrong Answer',
      lastAttempt: '2 days ago',
      bestRuntime: 'N/A',
      bestMemory: 'N/A',
      attempts: 3
    }
  ]
}

export default function Progress() {
  const [progressData] = useState(INITIAL_PROGRESS_DATA)
  const [selectedDifficulty, setSelectedDifficulty] = useState('All')

  const { stats, difficultyBreakdown, topicProgress, recentAttempts } = progressData

  const filteredAttempts = selectedDifficulty === 'All' 
    ? recentAttempts 
    : recentAttempts.filter(item => item.difficulty === selectedDifficulty)

  return (
    <div className="max-w-[1500px] mx-auto pb-12">
      
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
        <div>
          <h1 className="text-2xl font-bold text-slate-900">Learning Progress</h1>
          <p className="mt-1 text-sm text-slate-500">
            Monitor your algorithm mastery, success rates, streaks, and performance metrics.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <div className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-orange-50 border border-orange-100 text-orange-600 text-sm font-semibold">
            <Flame size={18} className="fill-orange-500" />
            <span>{stats.currentStreak} Day Streak</span>
          </div>
        </div>
      </div>

      {/* Top Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-8">
        
        {/* Solved Card */}
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">Problems Solved</span>
            <div className="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
              <CheckCircle2 size={18} />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-slate-900">{stats.problemsSolved}</span>
            <span className="text-xs text-slate-400 font-medium">/ {stats.problemsAttempted} Attempted</span>
          </div>
          <div className="mt-4 flex items-center gap-1.5 text-xs text-emerald-600 font-medium">
            <TrendingUp size={14} />
            <span>{((stats.problemsSolved / stats.problemsAttempted) * 100).toFixed(0)}% completion rate</span>
          </div>
        </div>

        {/* Accuracy Card */}
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">Accuracy</span>
            <div className="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
              <Target size={18} />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-slate-900">{stats.accuracy}%</span>
          </div>
          <div className="mt-4 flex items-center justify-between text-xs text-slate-500">
            <span>{stats.successfulAttempts} passing</span>
            <span>{stats.attemptCount} total runs</span>
          </div>
        </div>

        {/* Current & Best Streak */}
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">Consistency</span>
            <div className="w-9 h-9 rounded-xl bg-orange-50 text-orange-600 flex items-center justify-center">
              <Flame size={18} />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-slate-900">{stats.currentStreak}</span>
            <span className="text-xs text-slate-400 font-medium">Active Days</span>
          </div>
          <div className="mt-4 flex items-center justify-between text-xs text-slate-500">
            <span>Best Streak</span>
            <span className="font-semibold text-slate-700">{stats.bestStreak} Days</span>
          </div>
        </div>

        {/* Total Submissions */}
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">Total Attempts</span>
            <div className="w-9 h-9 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
              <BarChart2 size={18} />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-slate-900">{stats.attemptCount}</span>
            <span className="text-xs text-slate-400 font-medium">Submissions</span>
          </div>
          <div className="mt-4 flex items-center justify-between text-xs text-slate-500">
            <span>Avg Attempts/Problem</span>
            <span className="font-semibold text-slate-700">
              {(stats.attemptCount / stats.problemsAttempted).toFixed(1)}
            </span>
          </div>
        </div>

      </div>

      {/* Main Grid: Difficulty & Topic Breakdowns */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        
        {/* Difficulty Card */}
        <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
          <h2 className="text-base font-bold text-slate-900 mb-6">Difficulty Breakdown</h2>
          
          <div className="space-y-6">
            {/* Easy */}
            <div>
              <div className="flex justify-between text-sm mb-2 font-medium">
                <span className="text-emerald-700">Easy</span>
                <span className="text-slate-600">
                  {difficultyBreakdown.easy.solved} / {difficultyBreakdown.easy.total}
                </span>
              </div>
              <div className="h-2.5 w-full bg-slate-100 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-emerald-500 rounded-full" 
                  style={{ width: `${(difficultyBreakdown.easy.solved / difficultyBreakdown.easy.total) * 100}%` }}
                />
              </div>
            </div>

            {/* Medium */}
            <div>
              <div className="flex justify-between text-sm mb-2 font-medium">
                <span className="text-amber-700">Medium</span>
                <span className="text-slate-600">
                  {difficultyBreakdown.medium.solved} / {difficultyBreakdown.medium.total}
                </span>
              </div>
              <div className="h-2.5 w-full bg-slate-100 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-amber-500 rounded-full" 
                  style={{ width: `${(difficultyBreakdown.medium.solved / difficultyBreakdown.medium.total) * 100}%` }}
                />
              </div>
            </div>

            {/* Hard */}
            <div>
              <div className="flex justify-between text-sm mb-2 font-medium">
                <span className="text-rose-700">Hard</span>
                <span className="text-slate-600">
                  {difficultyBreakdown.hard.solved} / {difficultyBreakdown.hard.total}
                </span>
              </div>
              <div className="h-2.5 w-full bg-slate-100 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-rose-500 rounded-full" 
                  style={{ width: `${(difficultyBreakdown.hard.solved / difficultyBreakdown.hard.total) * 100}%` }}
                />
              </div>
            </div>
          </div>
        </div>

        {/* Topic-wise Progress */}
        <div className="lg:col-span-2 bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-base font-bold text-slate-900">Topic-wise Mastery</h2>
            <span className="text-xs text-slate-500">Based on attempted problem sets</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {topicProgress.map((item) => (
              <div key={item.topic} className="p-3.5 rounded-xl border border-slate-100 bg-slate-50/50">
                <div className="flex items-center justify-between text-sm font-medium mb-2">
                  <span className="text-slate-800 flex items-center gap-1.5">
                    <Layers size={15} className="text-blue-600" />
                    {item.topic}
                  </span>
                  <span className="text-xs text-slate-500">
                    {item.solved}/{item.total}
                  </span>
                </div>
                <div className="h-2 w-full bg-slate-200 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-blue-600 rounded-full"
                    style={{ width: `${item.percentage}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

      </div>

      {/* Attempt History Section */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-6">
          <div>
            <h2 className="text-base font-bold text-slate-900">Recent Problem Attempts</h2>
            <p className="text-xs text-slate-500 mt-0.5">Review your latest submissions and runtime efficiency.</p>
          </div>

          {/* Difficulty Filter */}
          <div className="flex items-center gap-2">
            <Filter size={15} className="text-slate-400" />
            <div className="flex bg-slate-100 p-1 rounded-xl text-xs font-medium text-slate-600">
              {['All', 'Easy', 'Medium', 'Hard'].map((diff) => (
                <button
                  key={diff}
                  onClick={() => setSelectedDifficulty(diff)}
                  className={`px-3 py-1 rounded-lg transition-all ${
                    selectedDifficulty === diff 
                      ? 'bg-white text-slate-900 shadow-sm font-semibold' 
                      : 'hover:text-slate-900'
                  }`}
                >
                  {diff}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Table */}
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead>
              <tr className="border-b border-slate-100 text-xs font-semibold text-slate-400 uppercase tracking-wider">
                <th className="pb-3 pl-2">Problem</th>
                <th className="pb-3">Topic</th>
                <th className="pb-3">Status</th>
                <th className="pb-3">Best Runtime</th>
                <th className="pb-3">Best Memory</th>
                <th className="pb-3">Last Attempt</th>
                <th className="pb-3 pr-2 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 text-slate-600">
              {filteredAttempts.map((item) => (
                <tr key={item.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="py-4 pl-2 font-medium text-slate-900">
                    <div className="flex items-center gap-2">
                      <span>{item.title}</span>
                      <span className={`px-2 py-0.5 text-[10px] font-semibold rounded-md ${
                        item.difficulty === 'Easy' ? 'bg-emerald-50 text-emerald-700' :
                        item.difficulty === 'Medium' ? 'bg-amber-50 text-amber-700' :
                        'bg-rose-50 text-rose-700'
                      }`}>
                        {item.difficulty}
                      </span>
                    </div>
                  </td>
                  <td className="py-4 text-slate-500">{item.topic}</td>
                  <td className="py-4">
                    <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-medium ${
                      item.status === 'Accepted' ? 'bg-emerald-50 text-emerald-700' : 'bg-rose-50 text-rose-700'
                    }`}>
                      {item.status}
                    </span>
                  </td>
                  <td className="py-4 font-mono text-xs text-slate-700">
                    <div className="flex items-center gap-1">
                      <Clock size={13} className="text-slate-400" />
                      {item.bestRuntime}
                    </div>
                  </td>
                  <td className="py-4 font-mono text-xs text-slate-700">
                    <div className="flex items-center gap-1">
                      <Cpu size={13} className="text-slate-400" />
                      {item.bestMemory}
                    </div>
                  </td>
                  <td className="py-4 text-xs text-slate-400">{item.lastAttempt}</td>
                  <td className="py-4 pr-2 text-right">
                    <Link
                      to={`/problem/${item.id}`}
                      className="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-medium text-slate-700 hover:bg-slate-50"
                    >
                      Solve Again
                      <ArrowUpRight size={13} />
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  )
}