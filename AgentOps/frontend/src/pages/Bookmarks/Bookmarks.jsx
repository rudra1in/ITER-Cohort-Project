import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import {
  Bookmark as BookmarkIcon,
  Trash2,
  ExternalLink,
  Search,
  CheckCircle2,
  FolderOpen
} from 'lucide-react'

// Demo bookmark records
const INITIAL_BOOKMARKS = [
  {
    id: 'two-sum',
    title: 'Two Sum',
    difficulty: 'Easy',
    topic: 'Arrays & Hashing',
    bookmarkedAt: 'Saved 2 days ago',
    status: 'Solved',
    notes: 'Remember the complementary hash map approach for O(n) runtime.'
  },
  {
    id: 'lru-cache',
    title: 'LRU Cache',
    difficulty: 'Medium',
    topic: 'Linked List / Hash Table',
    bookmarkedAt: 'Saved 4 days ago',
    status: 'Attempted',
    notes: 'Use doubly linked list combined with hash map for O(1) operations.'
  },
  {
    id: 'merge-k-sorted-lists',
    title: 'Merge k Sorted Lists',
    difficulty: 'Hard',
    topic: 'Heap / Divide & Conquer',
    bookmarkedAt: 'Saved 1 week ago',
    status: 'Unsolved',
    notes: 'Revise min-heap implementation and divide-and-conquer merge step.'
  },
  {
    id: 'binary-tree-maximum-path-sum',
    title: 'Binary Tree Maximum Path Sum',
    difficulty: 'Hard',
    topic: 'Trees / DFS',
    bookmarkedAt: 'Saved 2 weeks ago',
    status: 'Solved',
    notes: 'Post-order traversal computing max branch contribution.'
  }
]

export default function Bookmark() {
  const [bookmarks, setBookmarks] = useState(INITIAL_BOOKMARKS)
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedTopic, setSelectedTopic] = useState('All')

  // Remove handler ready for DELETE /api/bookmarks/:problemId
  const handleRemoveBookmark = (problemId) => {
    setBookmarks(prev => prev.filter(item => item.id !== problemId))
  }

  // Filter options
  const topics = ['All', ...new Set(bookmarks.map(b => b.topic))]

  const filteredBookmarks = bookmarks.filter(item => {
    const matchesSearch = item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          item.topic.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesTopic = selectedTopic === 'All' || item.topic === selectedTopic
    return matchesSearch && matchesTopic
  })

  return (
    <div className="max-w-[1500px] mx-auto pb-12">
      
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
        <div>
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center">
              <BookmarkIcon size={18} className="fill-blue-600" />
            </div>
            <h1 className="text-2xl font-bold text-slate-900">Bookmarked Problems</h1>
          </div>
          <p className="mt-1 text-sm text-slate-500">
            Quickly revisit important challenges, review custom approaches, and practice problem sets.
          </p>
        </div>

        <div className="text-sm text-slate-500 font-medium">
          Total Saved: <span className="font-bold text-slate-900">{bookmarks.length}</span>
        </div>
      </div>

      {/* Control Bar: Search & Category Filter */}
      <div className="bg-white border border-slate-200 rounded-2xl p-4 mb-6 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
        
        {/* Search */}
        <div className="relative w-full md:w-96">
          <Search size={16} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Search bookmarks by title or topic..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
          />
        </div>

        {/* Topic Filter Pills */}
        <div className="flex items-center gap-2 overflow-x-auto w-full md:w-auto pb-1 md:pb-0">
          {topics.map(topic => (
            <button
              key={topic}
              onClick={() => setSelectedTopic(topic)}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-medium whitespace-nowrap transition-all ${
                selectedTopic === topic
                  ? 'bg-blue-600 text-white shadow-sm font-semibold'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              {topic}
            </button>
          ))}
        </div>

      </div>

      {/* Bookmark Cards Grid */}
      {filteredBookmarks.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {filteredBookmarks.map((item) => (
            <div 
              key={item.id}
              className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm hover:shadow-md transition-shadow flex flex-col justify-between"
            >
              <div>
                {/* Card Top Details */}
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <div className="flex items-center gap-2">
                      <h2 className="text-lg font-bold text-slate-900 hover:text-blue-600 transition-colors">
                        <Link to={`/problem/${item.id}`}>{item.title}</Link>
                      </h2>
                      <span className={`px-2.5 py-0.5 rounded-md text-xs font-semibold ${
                        item.difficulty === 'Easy' ? 'bg-emerald-50 text-emerald-700' :
                        item.difficulty === 'Medium' ? 'bg-amber-50 text-amber-700' :
                        'bg-rose-50 text-rose-700'
                      }`}>
                        {item.difficulty}
                      </span>
                    </div>
                    <p className="mt-1 text-xs text-slate-500 font-medium">
                      {item.topic} · {item.bookmarkedAt}
                    </p>
                  </div>

                  {/* Remove Button */}
                  <button
                    onClick={() => handleRemoveBookmark(item.id)}
                    className="p-2 rounded-xl text-slate-400 hover:text-rose-600 hover:bg-rose-50 transition-colors"
                    title="Remove bookmark"
                  >
                    <Trash2 size={16} />
                  </button>
                </div>

                {/* Personal Notes / AI Summary Hint */}
                {item.notes && (
                  <div className="mt-4 p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs text-slate-600 leading-relaxed">
                    <strong className="text-slate-700 font-semibold">Key Note: </strong>
                    {item.notes}
                  </div>
                )}
              </div>

              {/* Bottom Action Footer */}
              <div className="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between">
                <div className="flex items-center gap-1.5 text-xs text-slate-500">
                  <CheckCircle2 size={14} className={item.status === 'Solved' ? 'text-emerald-500' : 'text-slate-300'} />
                  <span>Status: <strong className="text-slate-700">{item.status}</strong></span>
                </div>

                <Link
                  to={`/problem/${item.id}`}
                  className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-blue-50 text-blue-600 hover:bg-blue-100 text-xs font-semibold transition-colors"
                >
                  Open Workspace
                  <ExternalLink size={14} />
                </Link>
              </div>

            </div>
          ))}
        </div>
      ) : (
        /* Empty State */
        <div className="bg-white border border-slate-200 rounded-2xl p-12 text-center shadow-sm">
          <div className="w-14 h-14 rounded-2xl bg-slate-50 text-slate-400 flex items-center justify-center mx-auto mb-4">
            <FolderOpen size={26} />
          </div>
          <h2 className="text-lg font-bold text-slate-900">No bookmarks found</h2>
          <p className="mt-1 text-sm text-slate-500 max-w-sm mx-auto">
            {searchQuery ? "No saved problems matched your search term." : "You haven't bookmarked any problems yet. Click the bookmark icon in any problem workspace to save it."}
          </p>
          <Link
            to="/practice"
            className="mt-5 inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-blue-600 text-white text-sm font-semibold hover:bg-blue-700 transition-colors"
          >
            Explore Problems
          </Link>
        </div>
      )}

    </div>
  )
}