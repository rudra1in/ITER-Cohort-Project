import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Bell,
  ChevronDown,
  User,
  Settings,
  LogOut
} from 'lucide-react'

import { signOut } from 'firebase/auth'
import { auth } from '../../services/firebase'
import useAuth from '../../hooks/useAuth'


function TopNavbar() {

  const { user } = useAuth()
  const navigate = useNavigate()

  const [isOpen, setIsOpen] = useState(false)

  const dropdownRef = useRef(null)


  // Close dropdown when clicking outside
  useEffect(() => {

    const handleClickOutside = (event) => {

      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target)
      ) {
        setIsOpen(false)
      }

    }

    document.addEventListener('mousedown', handleClickOutside)

    return () => {
      document.removeEventListener('mousedown', handleClickOutside)
    }

  }, [])


  // Logout
  const handleLogout = async () => {

    try {

      await signOut(auth)

      setIsOpen(false)

      navigate('/login')

    } catch (error) {

      console.error('Logout failed:', error)

    }

  }


  // User information
  const displayName = user?.displayName || 'DSA Learner'

  const email = user?.email || ''

  const photoURL = user?.photoURL

  const initials = (
    user?.displayName ||
    user?.email ||
    'U'
  )
    .charAt(0)
    .toUpperCase()


  return (

    <header
      className="
        h-20
        bg-white
        border-b
        border-slate-200
        flex
        items-center
        justify-between
        px-6
        lg:px-8
      "
    >

      {/* ================================= */}
      {/* PAGE CONTEXT */}
      {/* ================================= */}

      <div>

        <p className="text-sm text-slate-500">
          DSA Coach
        </p>

        <p className="font-semibold text-slate-900">
          Your learning workspace
        </p>

      </div>


      {/* ================================= */}
      {/* RIGHT SECTION */}
      {/* ================================= */}

      <div className="flex items-center gap-4">

        {/* Notifications */}

        <button
          type="button"
          className="
            relative
            w-10
            h-10
            rounded-xl
            flex
            items-center
            justify-center
            text-slate-500
            hover:bg-slate-50
            hover:text-slate-900
            transition-colors
          "
          aria-label="Notifications"
        >

          <Bell size={19} />

          <span
            className="
              absolute
              top-2
              right-2
              w-1.5
              h-1.5
              rounded-full
              bg-blue-600
            "
          />

        </button>


        {/* ================================= */}
        {/* USER SECTION */}
        {/* ================================= */}

        <div
          ref={dropdownRef}
          className="relative"
        >

          {/* User button */}

          <button
            type="button"
            onClick={() => setIsOpen((prev) => !prev)}
            className="
              flex
              items-center
              gap-3
              pl-3
              pr-2
              py-2
              border-l
              border-slate-200
              rounded-xl
              hover:bg-slate-50
              transition-colors
            "
          >

            {/* Avatar */}

            <div
              className="
                w-9
                h-9
                rounded-full
                overflow-hidden
                bg-blue-100
                flex
                items-center
                justify-center
                shrink-0
              "
            >

              {photoURL ? (

                <img
                  src={photoURL}
                  alt={displayName}
                  className="w-full h-full object-cover"
                />

              ) : (

                <span
                  className="
                    text-sm
                    font-semibold
                    text-blue-700
                  "
                >
                  {initials}
                </span>

              )}

            </div>


            {/* User details */}

            <div className="hidden sm:block text-left">

              <p className="text-sm font-medium text-slate-900">
                {displayName}
              </p>

              <p className="text-xs text-slate-400 max-w-32 truncate">
                {email}
              </p>

            </div>


            <ChevronDown
              size={16}
              className={`
                hidden
                sm:block
                text-slate-400
                transition-transform
                ${isOpen ? 'rotate-180' : ''}
              `}
            />

          </button>


          {/* ================================= */}
          {/* DROPDOWN */}
          {/* ================================= */}

          {isOpen && (

            <div
              className="
                absolute
                right-0
                top-full
                mt-3
                w-64
                rounded-2xl
                border
                border-slate-200
                bg-white
                shadow-lg
                shadow-slate-200/50
                overflow-hidden
                z-50
              "
            >

              {/* User summary */}

              <div
                className="
                  px-4
                  py-4
                  border-b
                  border-slate-100
                "
              >

                <div className="flex items-center gap-3">

                  <div
                    className="
                      w-10
                      h-10
                      rounded-full
                      overflow-hidden
                      bg-blue-100
                      flex
                      items-center
                      justify-center
                      shrink-0
                    "
                  >

                    {photoURL ? (

                      <img
                        src={photoURL}
                        alt={displayName}
                        className="w-full h-full object-cover"
                      />

                    ) : (

                      <span
                        className="
                          text-sm
                          font-semibold
                          text-blue-700
                        "
                      >
                        {initials}
                      </span>

                    )}

                  </div>


                  <div className="min-w-0">

                    <p
                      className="
                        text-sm
                        font-semibold
                        text-slate-900
                        truncate
                      "
                    >
                      {displayName}
                    </p>

                    <p
                      className="
                        text-xs
                        text-slate-400
                        truncate
                      "
                    >
                      {email}
                    </p>

                  </div>

                </div>

              </div>


              {/* Menu items */}

              <div className="p-2">

                {/* Profile */}

                <button
                  type="button"
                  onClick={() => {
                    setIsOpen(false)
                    navigate('/profile')
                  }}
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
                    text-slate-600
                    hover:bg-slate-50
                    hover:text-slate-900
                    transition-colors
                  "
                >

                  <User size={17} />

                  <span>
                    Profile
                  </span>

                </button>


                {/* Settings */}

                <button
                  type="button"
                  onClick={() => {
                    setIsOpen(false)
                    navigate('/settings')
                  }}
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
                    text-slate-600
                    hover:bg-slate-50
                    hover:text-slate-900
                    transition-colors
                  "
                >

                  <Settings size={17} />

                  <span>
                    Settings
                  </span>

                </button>

              </div>


              {/* Logout */}

              <div
                className="
                  border-t
                  border-slate-100
                  p-2
                "
              >

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
                    text-red-600
                    hover:bg-red-50
                    transition-colors
                  "
                >

                  <LogOut size={17} />

                  <span>
                    Logout
                  </span>

                </button>

              </div>

            </div>

          )}

        </div>

      </div>

    </header>

  )
}


export default TopNavbar