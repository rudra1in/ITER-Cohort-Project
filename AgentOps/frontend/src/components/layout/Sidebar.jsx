import { Link, useLocation, useNavigate } from 'react-router-dom'

import {
  LayoutDashboard,
  Code2,
  Bot,
  Map,
  CircleHelp,
  Briefcase,
  Lightbulb,
  BarChart3,
  Bookmark,
  Settings,
  LogOut
} from 'lucide-react'

import { signOut } from 'firebase/auth'
import { auth } from '../../services/firebase'

function Sidebar() {
  const location = useLocation()

  const navigate = useNavigate()

  const navigationGroups = [
    {
      title: 'Workspace',

      items: [
        {
          name: 'Dashboard',
          path: '/dashboard',
          icon: LayoutDashboard
        },
        {
          name: 'Practice',
          path: '/practice',
          icon: Code2
        },
        {
          name: 'AI Coach',
          path: '/ai-coach',
          icon: Bot
        },
        {
          name: 'Roadmap',
          path: '/roadmap',
          icon: Map
        }
      ]
    },


    {
      title: 'Preparation',

      items: [
        {
          name: 'MCQ',
          path: '/mcq',
          icon: CircleHelp
        },
        {
          name: 'Interview Prep',
          path: '/interview',
          icon: Briefcase
        },
        {
          name: 'Tips',
          path: '/tips',
          icon: Lightbulb
        }
      ]
    },


    {
      title: 'Progress',

      items: [
        {
          name: 'Progress',
          path: '/progress',
          icon: BarChart3
        },
        {
          name: 'Bookmarks',
          path: '/bookmarks',
          icon: Bookmark
        }
      ]
    }
  ]


  /*
    Exact match for normal pages.

    For Practice:
    /practice
    /problem/two-sum
    /problem/valid-parentheses

    should all keep Practice highlighted.
  */
  const isActive = (path) => {

    if (path === '/practice') {
      return (
        location.pathname === '/practice' ||
        location.pathname.startsWith('/problem/')
      )
    }

    return location.pathname === path
  }

  const handleLogout = async () => {

    try {

      await signOut(auth)

      navigate('/login', { replace: true })

    } catch (error) {

      console.error('Logout failed:', error)

    }

  }


  return (

    <aside className="
      hidden
      lg:flex
      fixed
      left-0
      top-0
      bottom-0
      w-64
      bg-white
      border-r
      border-slate-200
      flex-col
      z-40
    ">


      {/* ================================================= */}
      {/* LOGO */}
      {/* ================================================= */}

      <div className="
        h-20
        px-6
        flex
        items-center
        border-b
        border-slate-100
        shrink-0
      ">

        <Link
          to="/dashboard"
          className="flex items-center gap-3"
        >

          <div className="
            w-9
            h-9
            rounded-xl
            bg-blue-600
            text-white
            flex
            items-center
            justify-center
            shadow-sm
          ">
            <Code2 size={20} />
          </div>


          <div>

            <p className="
              font-bold
              tracking-tight
              text-slate-900
            ">
              DSA Coach
            </p>


            <p className="
              text-[11px]
              text-slate-400
            ">
              AI-powered learning
            </p>

          </div>

        </Link>

      </div>


      {/* ================================================= */}
      {/* NAVIGATION */}
      {/* ================================================= */}

      <nav className="
        flex-1
        px-4
        py-6
        overflow-y-auto
      ">

        <div className="space-y-7">


          {navigationGroups.map((group) => (

            <div key={group.title}>


              {/* Group title */}

              <p className="
                px-3
                mb-3
                text-[11px]
                font-semibold
                uppercase
                tracking-wider
                text-slate-400
              ">
                {group.title}
              </p>


              {/* Group items */}

              <div className="space-y-1">

                {group.items.map((item) => {

                  const Icon = item.icon
                  const active = isActive(item.path)


                  return (

                    <Link
                      key={item.path}
                      to={item.path}
                      className={`
                        flex
                        items-center
                        gap-3
                        px-3
                        py-2.5
                        rounded-xl
                        text-sm
                        font-medium
                        transition-all
                        duration-200

                        ${
                          active
                            ? `
                              bg-blue-50
                              text-blue-700
                            `
                            : `
                              text-slate-600
                              hover:bg-slate-50
                              hover:text-slate-900
                            `
                        }
                      `}
                    >

                      <Icon
                        size={18}
                        strokeWidth={1.9}
                      />


                      <span>
                        {item.name}
                      </span>

                    </Link>

                  )

                })}

              </div>

            </div>

          ))}

        </div>

      </nav>


      {/* ================================================= */}
      {/* BOTTOM SECTION */}
      {/* ================================================= */}

      <div className="
        p-4
        border-t
        border-slate-100
        space-y-1
        shrink-0
      ">


        {/* Settings */}

        <Link
          to="/settings"
          className={`
            flex
            items-center
            gap-3
            px-3
            py-2.5
            rounded-xl
            text-sm
            font-medium
            transition-colors

            ${
              location.pathname === '/settings'
                ? 'bg-blue-50 text-blue-700'
                : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
            }
          `}
        >

          <Settings
            size={18}
            strokeWidth={1.9}
          />

          <span>
            Settings
          </span>

        </Link>


        {/* Logout */}

        <button
          type="button"
          onClick={handleLogout}
          className="
            w-full
            flex
            items-center
            gap-3
            px-3
            py-2.5
            rounded-xl
            text-sm
            font-medium
            text-slate-500
            hover:bg-red-50
            hover:text-red-600
            transition-colors
          "
        >

          <LogOut
            size={18}
            strokeWidth={1.9}
          />

          <span>
            Logout
          </span>

        </button>

      </div>

    </aside>

  )
}


export default Sidebar