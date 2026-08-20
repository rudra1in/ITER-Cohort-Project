import React, { useState } from 'react'
import {
  Lightbulb,
  Search,
  Zap,
  Gauge,
  Bug,
  Users,
  RotateCcw,
  GitMerge,
  AlertOctagon,
  ChevronRight,
  BookOpen,
  Bookmark,
  Sparkles
} from 'lucide-react'

const TIPS_DATABASE = [
  {
    id: 1,
    title: 'Break Problems into Small Testable Functions',
    category: 'Problem solving',
    difficulty: 'General',
    readTime: '2 min read',
    description: 'Before coding the full solution, split the algorithm into helpers (e.g., palindrome checker, node reverse, boundary validators).',
    actionPoints: [
      'Write down sample inputs and edge cases by hand first.',
      'Check constraints before selecting data structures (N <= 10^5 usually requires O(N) or O(N log N)).',
      'Explain your brute-force solution in under 2 minutes, then optimize.'
    ]
  },
  {
    id: 2,
    title: 'Recognize the Two-Pointer vs. Sliding Window Cue',
    category: 'Patterns',
    difficulty: 'Core Pattern',
    readTime: '3 min read',
    description: 'If you need contiguous subarrays with dynamic bounds, reach for sliding windows. If comparing pairs in sorted arrays, use two pointers.',
    actionPoints: [
      'Sliding window: Expand the right pointer, contract the left when the condition breaks.',
      'Two pointers from ends: Best for sorted pair sums or palindrome verifications.',
      'Fast & slow pointers: Cycle detection in linked lists and middle-node identification.'
    ]
  },
  {
    id: 3,
    title: 'Quick Mental Math for Time Complexity Constraints',
    category: 'Complexity',
    difficulty: 'Analysis',
    readTime: '2 min read',
    description: 'CP and interview judges typically allow ~10^8 operations per second. Use the input size N to decide which algorithm is viable.',
    actionPoints: [
      'N <= 20: Exponential O(2^N) or Backtracking.',
      'N <= 1000: O(N^2) Nested loops or Dynamic Programming.',
      'N <= 10^5: O(N log N) Sorting, Heaps, or Binary Search.',
      'N <= 10^9: O(log N) or O(1) Math / Binary search on answer.'
    ]
  },
  {
    id: 4,
    title: 'The "Rubber Duck" Debugging Technique for Coding Rounds',
    category: 'Debugging',
    difficulty: 'Troubleshooting',
    readTime: '3 min read',
    description: 'When an edge case fails, walk through your code with a small 2-3 element input array trace variable values line by line.',
    actionPoints: [
      'Check integer overflow conditions for large multiplications or addition.',
      'Inspect 0-index vs 1-index offsets and loop boundary conditions (<= vs <).',
      'Verify base cases in recursive functions before tracing recursive calls.'
    ]
  },
  {
    id: 5,
    title: 'How to Communicate During Technical Interviews',
    category: 'Interview',
    difficulty: 'Soft Skills',
    readTime: '4 min read',
    description: 'Never code in complete silence. Interviewers evaluate your thought clarity, trade-off analysis, and receptiveness to hints.',
    actionPoints: [
      'Ask clarifying questions: Are the elements sorted? Can there be negatives or duplicates?',
      'State time and space complexity before starting your implementation.',
      'Think aloud as you write your code, describing variable purposes.'
    ]
  },
  {
    id: 6,
    title: 'Avoid Common Off-By-One Errors in Binary Search',
    category: 'Common mistakes',
    difficulty: 'Pitfall Prevention',
    readTime: '2 min read',
    description: 'Binary search bugs often stem from mismatched loop bounds and midpoint calculation overflows.',
    actionPoints: [
      'Use mid = left + (right - left) / 2 instead of (left + right) / 2 to avoid overflow.',
      'If using left <= right, ensure updates are left = mid + 1 and right = mid - 1.',
      'Clarify lower-bound vs upper-bound requirements when handling duplicate items.'
    ]
  },
  {
    id: 7,
    title: 'Spaced Repetition Schedule for DSA Sheets',
    category: 'Revision',
    difficulty: 'Strategy',
    readTime: '3 min read',
    description: 'Do not solve a problem once and forget it. Revisit hard problems at scheduled intervals to build long-term muscle memory.',
    actionPoints: [
      'Day 1: Solve the problem with or without hints.',
      'Day 3: Re-code the optimal approach from memory without reading the solution.',
      'Day 7 & Day 21: Fast code outline and edge-case review.'
    ]
  }
]

const CATEGORIES = [
  { name: 'All', icon: Sparkles },
  { name: 'Problem solving', icon: Zap },
  { name: 'Complexity', icon: Gauge },
  { name: 'Debugging', icon: Bug },
  { name: 'Interview', icon: Users },
  { name: 'Revision', icon: RotateCcw },
  { name: 'Patterns', icon: GitMerge },
  { name: 'Common mistakes', icon: AlertOctagon }
]

function TipCard({ tip }) {
  const [expanded, setExpanded] = useState(false)

  return (
    <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow flex flex-col justify-between">
      <div>
        <div className="flex items-center justify-between gap-3 mb-3">
          <span className="px-2.5 py-1 rounded-md bg-blue-50 text-blue-700 text-xs font-semibold">
            {tip.category}
          </span>
          <span className="text-xs text-slate-400 font-medium">{tip.readTime}</span>
        </div>

        <h3 className="text-lg font-bold text-slate-900 leading-snug mb-2">
          {tip.title}
        </h3>

        <p className="text-sm text-slate-600 leading-relaxed">
          {tip.description}
        </p>

        {expanded && (
          <div className="mt-4 pt-4 border-t border-slate-100 space-y-2">
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
              Actionable Takeaways
            </h4>
            <ul className="space-y-1.5 text-xs text-slate-700 list-disc pl-4">
              {tip.actionPoints.map((point, index) => (
                <li key={index}>{point}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
        <button
          onClick={() => setExpanded(!expanded)}
          className="text-xs font-semibold text-blue-600 hover:text-blue-700 inline-flex items-center gap-1 cursor-pointer"
        >
          <span>{expanded ? 'Show Less' : 'View Action Points'}</span>
          <ChevronRight size={14} className={`transform transition-transform ${expanded ? 'rotate-90' : ''}`} />
        </button>
        <span className="text-[11px] font-medium text-slate-400 bg-slate-50 px-2 py-1 rounded-md">
          {tip.difficulty}
        </span>
      </div>
    </div>
  )
}

export default function Tips() {
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('All')

  const filteredTips = TIPS_DATABASE.filter(tip => {
    const matchesSearch =
      tip.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      tip.description.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesCategory = selectedCategory === 'All' || tip.category === selectedCategory
    return matchesSearch && matchesCategory
  })

  return (
    <div className="max-w-[1500px] mx-auto pb-12">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
        <div>
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
              <Lightbulb size={20} className="fill-blue-600/20" />
            </div>
            <h1 className="text-2xl font-bold text-slate-900">DSA & Interview Tips</h1>
          </div>
          <p className="mt-1 text-sm text-slate-500">
            Curated strategies, mental models, complexity rules, and communication techniques for technical coding rounds.
          </p>
        </div>

        <div className="text-sm text-slate-500 font-medium">
          Showing <span className="font-bold text-slate-900">{filteredTips.length}</span> tips
        </div>
      </div>

      {/* Control Bar: Search & Category Filter */}
      <div className="bg-white border border-slate-200 rounded-2xl p-4 mb-8 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
        {/* Search Input */}
        <div className="relative w-full md:w-96">
          <Search size={16} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Search strategies, patterns, mistakes..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
          />
        </div>

        {/* Category Pills */}
        <div className="flex items-center gap-2 overflow-x-auto w-full md:w-auto pb-1 md:pb-0">
          {CATEGORIES.map(cat => {
            const Icon = cat.icon
            const active = selectedCategory === cat.name
            return (
              <button
                key={cat.name}
                onClick={() => setSelectedCategory(cat.name)}
                className={`inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-medium whitespace-nowrap transition-all cursor-pointer ${
                  active
                    ? 'bg-blue-600 text-white shadow-sm font-semibold'
                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                <Icon size={14} />
                <span>{cat.name}</span>
              </button>
            )
          })}
        </div>
      </div>

      {/* Tips Grid */}
      {filteredTips.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredTips.map(tip => (
            <TipCard key={tip.id} tip={tip} />
          ))}
        </div>
      ) : (
        <div className="bg-white border border-slate-200 rounded-2xl p-12 text-center shadow-sm">
          <BookOpen size={32} className="text-slate-400 mx-auto mb-3" />
          <h3 className="text-lg font-bold text-slate-900">No tips found</h3>
          <p className="text-sm text-slate-500 mt-1">
            Try adjusting your search terms or picking another category.
          </p>
        </div>
      )}
    </div>
  )
}