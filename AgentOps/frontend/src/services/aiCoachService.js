// ============================================================
// AI COACH SERVICE
// ============================================================
//
// communication layer between the AI Coach UI
// and the FastAPI AI agent.
// 
// Flow:
//
// AICoach.jsx
//      ↓
// getCoachResponse()
//      ↓
// FastAPI /api/coach/ask
//      ↓
// LangGraph
//      ↓
// Router
//      ↓
// Specialized Agent
//      ↓
// RAG + LLM
//      ↓
// Response
//
// ============================================================

// ============================================================
// CONFIGURATION
// ============================================================

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'


// ============================================================
// MOCK RESPONSES
// ============================================================
//
// These are temporary responses only.
// They allow the entire UI to work before FastAPI is connected.
//
// The backend will eventually generate dynamic responses based
// on:
//
// - problem
// - code
// - language
// - mode
// - conversation
// - user message
//
// ============================================================

/*const mockResponses = {

  hint: {
    default:
      'Think about what information you need to remember while moving through the input. Can you avoid checking every possible pair?'
  },

  explain: {
    default:
      'Start by identifying the main operation the problem asks you to perform. Then look for a data structure that can make that operation faster.'
  },

  analyze: {
    default:
      'Before changing your code, trace it manually with a small example. Check the first point where the actual result differs from the expected result.'
  },

  review: {
    default:
      'I can review your solution for correctness, time complexity, space complexity, and edge cases. Once the FastAPI execution and AI backend are connected, I can analyze your actual code in detail.'
  }

}*/


// ============================================================
// BUILD REQUEST PAYLOAD
// ============================================================

function buildCoachPayload({
  message,
  mode,
  language,
  code,
  problem,
  conversation,
  thread_id
}) {

  return {

    // User's current message
    message,

    // Current coaching mode
    mode: mode || "explain",

    // Programming language
    language: language || "java",

    // User's submitted code
    code: code || "",

    // Current DSA problem
    problem:
      problem
        ? {
            id: problem.id,
            title: problem.title,
            difficulty: problem.difficulty,
            topic: problem.topic,
            pattern: problem.pattern,
            description: problem.description,
            examples: problem.examples || [],
            constraints: problem.constraints || []
          }
        : null,

    // Frontend conversation history
    conversation: conversation || [],

    // LangGraph conversation identifier
    thread_id

  }

}



// ============================================================
// MOCK MODE
// ============================================================
//
// This keeps the frontend completely functional before the
// FastAPI backend exists.
//
// ============================================================

/*async function getMockCoachResponse({
  mode
}) {

  // Simulate network/AI thinking time.

  await new Promise((resolve) => {
    setTimeout(resolve, 900)
  })


  return (
    mockResponses[mode]?.default ||
    mockResponses.hint.default
  )

}*/


// ============================================================
// FASTAPI REQUEST
// ============================================================

async function getFastAPIResponse(payload) {

  console.log("====================================");
  console.log("AI COACH REQUEST");
  console.log("====================================");
  console.log("Message:", payload.message);
  console.log("Mode:", payload.mode);
  console.log("Language:", payload.language);
  console.log("Code:", payload.code);
  console.log("Problem:", payload.problem);
  console.log("Thread ID:", payload.thread_id);
  console.log("====================================");


  const response = await fetch(
    `${API_BASE_URL}/api/coach/ask`,
    {
      method: 'POST',

      headers: {
        'Content-Type': 'application/json'
      },

      body: JSON.stringify({
        message: payload.message,
        mode: payload.mode || 'explain',
        language: payload.language || 'java',
        code: payload.code || '',
        problem: payload.problem || null,
        conversation: payload.conversation || [],
        thread_id: payload.thread_id
      })
    }
  )


  if (!response.ok) {

    let errorMessage =
      `AI Coach request failed with status ${response.status}`

    try {

      const errorData =
        await response.json()

      if (errorData?.detail) {
        errorMessage = errorData.detail
      }

    } catch {
      // Keep default error message.
    }

    throw new Error(errorMessage)
  }


  const data = await response.json()

  console.log("====================================");
  console.log("AI COACH RESPONSE");
  console.log("====================================");
  console.log(data);
  console.log("Agent Type:", data?.agent_type);
  console.log("Evaluation:", data?.evaluation);
  console.log("Retry Count:", data?.retry_count);
  console.log("====================================");

  if (!data?.answer) {

    throw new Error(
      'AI Coach returned an invalid response.'
    )

  }

  let answer = data.answer

  // ----------------------------------------------------------
  // HANDLE OBJECT ANSWERS
  // ----------------------------------------------------------

  if (typeof answer === 'object' && answer !== null) {
    answer =
      answer.answer ||
      answer.response ||
      answer.content ||
      JSON.stringify(answer)
  }

  if (typeof answer !== 'string') {
    throw new Error(
      'AI Coach returned an invalid answer.'
    )
  }

  return data
}


// ============================================================
// GET COACH RESPONSE
// ============================================================
//
// THIS is the only function AICoach.jsx needs.
//
// ============================================================

//const USE_MOCK_AI = false


export async function getCoachResponse({

  message,

  mode,

  language,

  code,

  problem,

  conversation,

  thread_id,

}) {

  const payload =
    buildCoachPayload({
      message,
      mode,
      language,
      code,
      problem,
      conversation,
      thread_id
    })


  // ----------------------------------------------------------
  // Development logging
  // ----------------------------------------------------------

  console.log("AI Coach request:", payload);

  // ==========================================================
  // FASTAPI
  // ==========================================================

  return await getFastAPIResponse(payload);
}
