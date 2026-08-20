import {
  Mail,
  Calendar,
  ShieldCheck,
  LogOut,
  ArrowLeft
} from 'lucide-react'

import { useNavigate } from 'react-router-dom'

import { signOut } from 'firebase/auth'
import { auth } from '../../services/firebase'

import useAuth from '../../hooks/useAuth'


function Profile() {

  const { user } = useAuth()
  const navigate = useNavigate()


  const displayName =
    user?.displayName || 'DSA Learner'

  const email =
    user?.email || 'No email available'

  const photoURL =
    user?.photoURL

  const initials = (
    user?.displayName ||
    user?.email ||
    'U'
  )
    .charAt(0)
    .toUpperCase()


  const provider = user?.providerData?.[0]?.providerId


  const getProviderName = () => {

    if (provider === 'google.com') {
      return 'Google'
    }

    if (provider === 'github.com') {
      return 'GitHub'
    }

    if (provider === 'password') {
      return 'Email & Password'
    }

    return 'Firebase Authentication'
  }


  const handleLogout = async () => {

    try {

      await signOut(auth)

      navigate('/login')

    } catch (error) {

      console.error('Logout failed:', error)

    }

  }


  const createdAt = user?.metadata?.creationTime

    ? new Date(user.metadata.creationTime).toLocaleDateString(
        'en-IN',
        {
          day: 'numeric',
          month: 'long',
          year: 'numeric'
        }
      )

    : 'Not available'


  return (

    <div className="max-w-5xl mx-auto space-y-8 pb-10">


      {/* ========================================= */}
      {/* HEADER */}
      {/* ========================================= */}

      <section>

        <button
          type="button"
          onClick={() => navigate('/dashboard')}
          className="
            inline-flex
            items-center
            gap-2
            text-sm
            font-medium
            text-slate-500
            hover:text-slate-900
            transition
          "
        >

          <ArrowLeft size={16} />

          Back to dashboard

        </button>


        <div className="mt-5">

          <p className="
            text-sm
            font-medium
            text-blue-600
          ">
            Account
          </p>

          <h1 className="
            mt-1
            text-3xl
            font-bold
            tracking-tight
            text-slate-900
          ">
            Your Profile
          </h1>

          <p className="
            mt-2
            text-slate-500
          ">
            Manage your account information and authentication details.
          </p>

        </div>

      </section>


      {/* ========================================= */}
      {/* PROFILE CARD */}
      {/* ========================================= */}

      <section className="
        rounded-2xl
        border
        border-slate-200
        bg-white
        shadow-sm
        overflow-hidden
      ">


        {/* Profile hero */}

        <div className="
          px-6
          py-8
          lg:px-8
          bg-slate-50
          border-b
          border-slate-200
        ">

          <div className="
            flex
            flex-col
            sm:flex-row
            sm:items-center
            gap-5
          ">


            {/* Avatar */}

            <div className="
              w-24
              h-24
              rounded-2xl
              overflow-hidden
              bg-blue-100
              flex
              items-center
              justify-center
              shrink-0
              border
              border-white
              shadow-sm
            ">

              {photoURL ? (

                <img
                  src={photoURL}
                  alt={displayName}
                  className="
                    w-full
                    h-full
                    object-cover
                  "
                />

              ) : (

                <span className="
                  text-3xl
                  font-bold
                  text-blue-700
                ">
                  {initials}
                </span>

              )}

            </div>


            {/* Name */}

            <div>

              <h2 className="
                text-2xl
                font-bold
                text-slate-900
              ">
                {displayName}
              </h2>

              <p className="
                mt-1
                text-sm
                text-slate-500
              ">
                {email}
              </p>

              <div className="
                mt-3
                inline-flex
                items-center
                gap-2
                px-2.5
                py-1
                rounded-full
                bg-blue-50
                text-blue-700
                text-xs
                font-semibold
              ">

                <ShieldCheck size={14} />

                Account verified

              </div>

            </div>

          </div>

        </div>


        {/* ========================================= */}
        {/* ACCOUNT INFORMATION */}
        {/* ========================================= */}

        <div className="p-6 lg:p-8">

          <h3 className="
            text-lg
            font-bold
            text-slate-900
          ">
            Account information
          </h3>

          <p className="
            mt-1
            text-sm
            text-slate-500
          ">
            Information associated with your Firebase account.
          </p>


          <div className="
            mt-6
            grid
            grid-cols-1
            md:grid-cols-2
            gap-4
          ">


            {/* Email */}

            <div className="
              rounded-xl
              border
              border-slate-200
              p-4
            ">

              <div className="
                flex
                items-center
                gap-3
              ">

                <div className="
                  w-9
                  h-9
                  rounded-lg
                  bg-blue-50
                  text-blue-600
                  flex
                  items-center
                  justify-center
                ">

                  <Mail size={17} />

                </div>

                <div>

                  <p className="
                    text-xs
                    text-slate-400
                  ">
                    Email
                  </p>

                  <p className="
                    mt-0.5
                    text-sm
                    font-medium
                    text-slate-900
                    break-all
                  ">
                    {email}
                  </p>

                </div>

              </div>

            </div>


            {/* Provider */}

            <div className="
              rounded-xl
              border
              border-slate-200
              p-4
            ">

              <div className="
                flex
                items-center
                gap-3
              ">

                <div className="
                  w-9
                  h-9
                  rounded-lg
                  bg-violet-50
                  text-violet-600
                  flex
                  items-center
                  justify-center
                ">

                  <ShieldCheck size={17} />

                </div>

                <div>

                  <p className="
                    text-xs
                    text-slate-400
                  ">
                    Sign-in method
                  </p>

                  <p className="
                    mt-0.5
                    text-sm
                    font-medium
                    text-slate-900
                  ">
                    {getProviderName()}
                  </p>

                </div>

              </div>

            </div>


            {/* Created */}

            <div className="
              rounded-xl
              border
              border-slate-200
              p-4
            ">

              <div className="
                flex
                items-center
                gap-3
              ">

                <div className="
                  w-9
                  h-9
                  rounded-lg
                  bg-emerald-50
                  text-emerald-600
                  flex
                  items-center
                  justify-center
                ">

                  <Calendar size={17} />

                </div>

                <div>

                  <p className="
                    text-xs
                    text-slate-400
                  ">
                    Account created
                  </p>

                  <p className="
                    mt-0.5
                    text-sm
                    font-medium
                    text-slate-900
                  ">
                    {createdAt}
                  </p>

                </div>

              </div>

            </div>


            {/* Firebase UID */}

            <div className="
              rounded-xl
              border
              border-slate-200
              p-4
            ">

              <div>

                <p className="
                  text-xs
                  text-slate-400
                ">
                  User ID
                </p>

                <p className="
                  mt-1
                  text-xs
                  font-mono
                  text-slate-600
                  break-all
                ">
                  {user?.uid || 'Not available'}
                </p>

              </div>

            </div>

          </div>

        </div>

      </section>


      {/* ========================================= */}
      {/* ACCOUNT ACTIONS */}
      {/* ========================================= */}

      <section className="
        rounded-2xl
        border
        border-slate-200
        bg-white
        shadow-sm
        p-6
        lg:p-8
      ">

        <h3 className="
          text-lg
          font-bold
          text-slate-900
        ">
          Account actions
        </h3>

        <p className="
          mt-1
          text-sm
          text-slate-500
        ">
          Manage your current session.
        </p>


        <div className="
          mt-5
          flex
          flex-col
          sm:flex-row
          sm:items-center
          sm:justify-between
          gap-4
          rounded-xl
          border
          border-red-100
          bg-red-50/50
          p-4
        ">

          <div>

            <p className="
              text-sm
              font-semibold
              text-slate-900
            ">
              Sign out of DSA Coach
            </p>

            <p className="
              mt-1
              text-xs
              text-slate-500
            ">
              You can sign back in anytime.
            </p>

          </div>


          <button
            type="button"
            onClick={handleLogout}
            className="
              inline-flex
              items-center
              justify-center
              gap-2
              px-4
              py-2.5
              rounded-xl
              bg-white
              border
              border-red-200
              text-sm
              font-semibold
              text-red-600
              hover:bg-red-50
              transition
              shrink-0
            "
          >

            <LogOut size={16} />

            Sign out

          </button>

        </div>

      </section>

    </div>

  )
}


export default Profile