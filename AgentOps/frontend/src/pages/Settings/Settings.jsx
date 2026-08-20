import { useState } from 'react'
import {
  User,
  Mail,
  Shield,
  LogOut,
  Trash2,
  Save,
  CheckCircle2
} from 'lucide-react'
import { updateProfile, signOut } from 'firebase/auth'
import { useNavigate } from 'react-router-dom'

import { auth } from '../../services/firebase'
import useAuth from '../../hooks/useAuth'

function Settings() {

  const { user } = useAuth()
  const navigate = useNavigate()

  const [name, setName] = useState(user?.displayName || '')
  const [saving, setSaving] = useState(false)
  const [saved, setSaved] = useState(false)
  const [error, setError] = useState('')

  const handleSaveProfile = async (e) => {

    e.preventDefault()

    if (!user) return

    setSaving(true)
    setSaved(false)
    setError('')

    try {

      await updateProfile(user, {
        displayName: name.trim()
      })

      setSaved(true)

      setTimeout(() => {
        setSaved(false)
      }, 3000)

    } catch (err) {

      console.error(err)

      setError('Unable to update your profile. Please try again.')

    } finally {

      setSaving(false)

    }
  }


  const handleLogout = async () => {

    try {

      await signOut(auth)

      navigate('/login')

    } catch (err) {

      console.error(err)

    }
  }


  if (!user) {
    return null
  }


  return (
    <div className="max-w-5xl mx-auto space-y-8 pb-10">

      {/* Header */}

      <div>

        <h1 className="text-3xl font-bold tracking-tight text-slate-900">
          Settings
        </h1>

        <p className="mt-2 text-slate-500">
          Manage your account and learning preferences.
        </p>

      </div>


      {/* Profile */}

      <section className="bg-white border border-slate-200 rounded-2xl shadow-sm">

        <div className="p-6 border-b border-slate-100">

          <div className="flex items-center gap-3">

            <div className="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
              <User size={20} />
            </div>

            <div>

              <h2 className="font-semibold text-slate-900">
                Profile
              </h2>

              <p className="text-sm text-slate-500">
                Update your personal information.
              </p>

            </div>

          </div>

        </div>


        <form
          onSubmit={handleSaveProfile}
          className="p-6 space-y-6"
        >

          {/* Profile picture */}

          <div className="flex items-center gap-4">

            <div className="
              w-16
              h-16
              rounded-full
              overflow-hidden
              bg-blue-100
              flex
              items-center
              justify-center
              shrink-0
            ">

              {user.photoURL ? (

                <img
                  src={user.photoURL}
                  alt={user.displayName || 'User'}
                  className="w-full h-full object-cover"
                />

              ) : (

                <span className="text-xl font-bold text-blue-700">
                  {(user.displayName || user.email || 'U')
                    .charAt(0)
                    .toUpperCase()}
                </span>

              )}

            </div>


            <div>

              <p className="font-semibold text-slate-900">
                {user.displayName || 'DSA Learner'}
              </p>

              <p className="text-sm text-slate-400">
                {user.email}
              </p>

            </div>

          </div>


          {/* Name */}

          <div>

            <label className="block text-sm font-medium text-slate-700 mb-2">
              Full name
            </label>

            <div className="relative">

              <User
                size={18}
                className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"
              />

              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Your name"
                className="
                  w-full
                  h-12
                  rounded-xl
                  border border-slate-200
                  bg-white
                  pl-11
                  pr-4
                  text-sm
                  outline-none
                  focus:border-blue-500
                  focus:ring-4
                  focus:ring-blue-500/10
                "
              />

            </div>

          </div>


          {/* Email */}

          <div>

            <label className="block text-sm font-medium text-slate-700 mb-2">
              Email
            </label>

            <div className="relative">

              <Mail
                size={18}
                className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"
              />

              <input
                type="email"
                value={user.email || ''}
                disabled
                className="
                  w-full
                  h-12
                  rounded-xl
                  border border-slate-200
                  bg-slate-50
                  pl-11
                  pr-4
                  text-sm
                  text-slate-500
                  cursor-not-allowed
                "
              />

            </div>

            <p className="mt-2 text-xs text-slate-400">
              Your email is managed by your authentication provider.
            </p>

          </div>


          {/* Error */}

          {error && (

            <div className="rounded-xl bg-red-50 border border-red-100 px-4 py-3 text-sm text-red-600">
              {error}
            </div>

          )}


          {/* Saved */}

          {saved && (

            <div className="flex items-center gap-2 rounded-xl bg-emerald-50 border border-emerald-100 px-4 py-3 text-sm text-emerald-700">

              <CheckCircle2 size={17} />

              Profile updated successfully.

            </div>

          )}


          {/* Save */}

          <button
            type="submit"
            disabled={saving}
            className="
              inline-flex
              items-center
              justify-center
              gap-2
              px-5
              py-2.5
              rounded-xl
              bg-blue-600
              hover:bg-blue-700
              disabled:opacity-60
              text-white
              text-sm
              font-semibold
              transition
            "
          >

            <Save size={16} />

            {saving ? 'Saving...' : 'Save changes'}

          </button>

        </form>

      </section>


      {/* Account */}

      <section className="bg-white border border-slate-200 rounded-2xl shadow-sm">

        <div className="p-6 border-b border-slate-100">

          <div className="flex items-center gap-3">

            <div className="w-10 h-10 rounded-xl bg-slate-100 text-slate-600 flex items-center justify-center">
              <Shield size={20} />
            </div>

            <div>

              <h2 className="font-semibold text-slate-900">
                Account
              </h2>

              <p className="text-sm text-slate-500">
                Manage your authentication and account access.
              </p>

            </div>

          </div>

        </div>


        <div className="p-6 space-y-4">

          {/* Provider */}

          <div className="flex items-center justify-between gap-4 p-4 rounded-xl bg-slate-50">

            <div>

              <p className="text-sm font-medium text-slate-900">
                Authentication provider
              </p>

              <p className="text-xs text-slate-400 mt-1">
                {user.providerData?.[0]?.providerId || 'Firebase'}
              </p>

            </div>

            <span className="px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold">
              Active
            </span>

          </div>


          {/* Logout */}

          <button
            type="button"
            onClick={handleLogout}
            className="
              w-full
              flex
              items-center
              justify-between
              p-4
              rounded-xl
              border
              border-slate-200
              hover:border-red-200
              hover:bg-red-50
              transition
              text-left
            "
          >

            <div className="flex items-center gap-3">

              <div className="w-9 h-9 rounded-lg bg-slate-100 text-slate-500 flex items-center justify-center">
                <LogOut size={17} />
              </div>

              <div>

                <p className="text-sm font-semibold text-slate-900">
                  Sign out
                </p>

                <p className="text-xs text-slate-400">
                  Sign out of your DSA Coach account.
                </p>

              </div>

            </div>

            <span className="text-sm font-medium text-slate-500">
              Logout
            </span>

          </button>


          {/* Delete */}

          <div className="flex items-center justify-between gap-4 p-4 rounded-xl border border-red-100">

            <div className="flex items-center gap-3">

              <div className="w-9 h-9 rounded-lg bg-red-50 text-red-500 flex items-center justify-center">
                <Trash2 size={17} />
              </div>

              <div>

                <p className="text-sm font-semibold text-slate-900">
                  Delete account
                </p>

                <p className="text-xs text-slate-400">
                  Account deletion will be implemented later.
                </p>

              </div>

            </div>

            <button
              type="button"
              disabled
              className="
                px-3
                py-2
                rounded-lg
                bg-slate-100
                text-slate-400
                text-xs
                font-semibold
                cursor-not-allowed
              "
            >
              Coming soon
            </button>

          </div>

        </div>

      </section>

    </div>
  )
}

export default Settings