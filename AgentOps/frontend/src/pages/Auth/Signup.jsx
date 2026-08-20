import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import {
  User,
  Mail,
  Lock,
  Eye,
  EyeOff,
  ArrowRight
} from 'lucide-react'

import {
  createUserWithEmailAndPassword,
  updateProfile,
  GoogleAuthProvider,
  GithubAuthProvider,
  signInWithPopup
} from 'firebase/auth'

import { auth } from '../../services/firebase'

import AuthLayout from '../../components/common/AuthLayout'
import SocialAuth from '../../components/common/SocialAuth'
import AuthDivider from '../../components/common/AuthDivider'


function Signup() {

  const navigate = useNavigate()

  const [showPassword, setShowPassword] = useState(false)

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: ''
  })

  const [loading, setLoading] = useState(false)

  const [error, setError] = useState('')


  // =========================================
  // INPUT CHANGE
  // =========================================

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })

    if (error) {
      setError('')
    }
  }


  // =========================================
  // EMAIL / PASSWORD SIGNUP
  // =========================================

  const handleSubmit = async (e) => {

    e.preventDefault()

    setError('')
    setLoading(true)

    try {

      // Create Firebase account
      const result = await createUserWithEmailAndPassword(
        auth,
        formData.email,
        formData.password
      )

      // Add user's name to Firebase profile
      await updateProfile(result.user, {
        displayName: formData.name
      })

      console.log('Created user:', result.user)

      // Go to dashboard
      navigate('/dashboard')

    } catch (error) {

      console.error('Signup error:', error)

      switch (error.code) {

        case 'auth/email-already-in-use':
          setError(
            'An account already exists with this email.'
          )
          break

        case 'auth/invalid-email':
          setError(
            'Please enter a valid email address.'
          )
          break

        case 'auth/weak-password':
          setError(
            'Password should be at least 6 characters.'
          )
          break

        case 'auth/operation-not-allowed':
          setError(
            'Email/password authentication is not enabled in Firebase.'
          )
          break

        default:
          setError(
            'Unable to create your account. Please try again.'
          )
      }

    } finally {

      setLoading(false)

    }
  }


  // =========================================
  // GOOGLE SIGNUP
  // =========================================

  const handleGoogleSignup = async () => {

    setError('')
    setLoading(true)

    try {

      const provider = new GoogleAuthProvider()

      const result = await signInWithPopup(
        auth,
        provider
      )

      console.log('Google user:', result.user)

      navigate('/dashboard')

    } catch (error) {

      console.error('Google signup error:', error)

      if (error.code !== 'auth/popup-closed-by-user') {

        setError(
          'Google sign-up failed. Please try again.'
        )

      }

    } finally {

      setLoading(false)

    }
  }


  // =========================================
  // GITHUB SIGNUP
  // =========================================

  const handleGithubSignup = async () => {

    setError('')
    setLoading(true)

    try {

      const provider = new GithubAuthProvider()

      const result = await signInWithPopup(
        auth,
        provider
      )

      console.log('GitHub user:', result.user)

      navigate('/dashboard')

    } catch (error) {

      console.error('GitHub signup error:', error)

      if (error.code !== 'auth/popup-closed-by-user') {

        setError(
          'GitHub sign-up failed. Please try again.'
        )

      }

    } finally {

      setLoading(false)

    }
  }


  return (

    <AuthLayout>

      {/* ========================================= */}
      {/* HEADING */}
      {/* ========================================= */}

      <div className="mb-8">

        <h2 className="text-3xl font-bold tracking-tight">
          Create your account
        </h2>

        <p className="mt-2 text-slate-500">
          Start building stronger DSA skills today.
        </p>

      </div>


      {/* ========================================= */}
      {/* SOCIAL AUTH */}
      {/* ========================================= */}

      <SocialAuth
        onGoogle={handleGoogleSignup}
        onGithub={handleGithubSignup}
      />


      <AuthDivider />


      {/* ========================================= */}
      {/* ERROR */}
      {/* ========================================= */}

      {error && (

        <div className="
          mb-5
          rounded-xl
          border
          border-red-200
          bg-red-50
          px-4
          py-3
          text-sm
          text-red-600
        ">

          {error}

        </div>

      )}


      {/* ========================================= */}
      {/* SIGNUP FORM */}
      {/* ========================================= */}

      <form
        onSubmit={handleSubmit}
        className="space-y-5"
      >

        {/* Name */}

        <div>

          <label className="block text-sm font-medium mb-2">
            Full name
          </label>

          <div className="relative">

            <User
              size={18}
              className="
                absolute
                left-3.5
                top-1/2
                -translate-y-1/2
                text-slate-400
              "
            />

            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Your name"
              required
              disabled={loading}
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
                transition
                placeholder:text-slate-400
                focus:border-blue-500
                focus:ring-4
                focus:ring-blue-500/10
                disabled:opacity-60
              "
            />

          </div>

        </div>


        {/* Email */}

        <div>

          <label className="block text-sm font-medium mb-2">
            Email
          </label>

          <div className="relative">

            <Mail
              size={18}
              className="
                absolute
                left-3.5
                top-1/2
                -translate-y-1/2
                text-slate-400
              "
            />

            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="you@example.com"
              required
              disabled={loading}
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
                transition
                placeholder:text-slate-400
                focus:border-blue-500
                focus:ring-4
                focus:ring-blue-500/10
                disabled:opacity-60
              "
            />

          </div>

        </div>


        {/* Password */}

        <div>

          <label className="block text-sm font-medium mb-2">
            Password
          </label>

          <div className="relative">

            <Lock
              size={18}
              className="
                absolute
                left-3.5
                top-1/2
                -translate-y-1/2
                text-slate-400
              "
            />

            <input
              type={showPassword ? 'text' : 'password'}
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Create a password"
              minLength={6}
              required
              disabled={loading}
              className="
                w-full
                h-12
                rounded-xl
                border border-slate-200
                bg-white
                pl-11
                pr-11
                text-sm
                outline-none
                transition
                placeholder:text-slate-400
                focus:border-blue-500
                focus:ring-4
                focus:ring-blue-500/10
                disabled:opacity-60
              "
            />


            <button
              type="button"
              disabled={loading}
              onClick={() =>
                setShowPassword(!showPassword)
              }
              className="
                absolute
                right-3.5
                top-1/2
                -translate-y-1/2
                text-slate-400
                hover:text-slate-600
                transition
                disabled:opacity-50
              "
            >

              {showPassword
                ? <EyeOff size={18} />
                : <Eye size={18} />
              }

            </button>

          </div>

        </div>


        {/* ========================================= */}
        {/* TERMS */}
        {/* ========================================= */}

        <label className="flex items-start gap-3 cursor-pointer">

          <input
            type="checkbox"
            required
            disabled={loading}
            className="mt-1 accent-blue-600"
          />

          <span className="text-sm text-slate-500 leading-relaxed">

            I agree to the terms and conditions and understand
            that my learning progress will be stored in my account.

          </span>

        </label>


        {/* ========================================= */}
        {/* SUBMIT */}
        {/* ========================================= */}

        <button
          type="submit"
          disabled={loading}
          className="
            w-full
            h-12
            rounded-xl
            bg-blue-600
            hover:bg-blue-700
            disabled:bg-blue-400
            text-white
            font-semibold
            flex
            items-center
            justify-center
            gap-2
            transition
            shadow-sm
            hover:shadow-md
            disabled:cursor-not-allowed
          "
        >

          {loading
            ? 'Creating account...'
            : 'Create Account'
          }

          {!loading && (
            <ArrowRight size={18} />
          )}

        </button>

      </form>


      {/* ========================================= */}
      {/* LOGIN LINK */}
      {/* ========================================= */}

      <p className="mt-7 text-center text-sm text-slate-500">

        Already have an account?{' '}

        <Link
          to="/login"
          className="
            font-semibold
            text-blue-600
            hover:text-blue-700
          "
        >
          Sign in
        </Link>

      </p>

    </AuthLayout>
  )
}


export default Signup