// ============================================================
// INTERVIEW PREP SERVICE
// ============================================================
//
// CURRENT:
// Uses local mock data so the Interview Prep page works
// completely without a backend.
//
// LATER:
// Replace the functions in this file with requests to the
// FastAPI Interview Agent.
//
// InterviewPrep.jsx should NOT need major changes when the
// backend is connected.
//
// ============================================================


// ============================================================
// INTERVIEW CATEGORIES
// ============================================================

const interviewCategories = [

  {
    id: 'technical',
    name: 'Technical Interview',
    description:
      'Core programming and software development questions.',
    questionCount: 8
  },

  {
    id: 'dsa',
    name: 'DSA Interview',
    description:
      'Algorithms, data structures, and problem-solving.',
    questionCount: 8
  },

  {
    id: 'sql',
    name: 'SQL & DBMS',
    description:
      'SQL queries, databases, normalization, and transactions.',
    questionCount: 7
  },

  {
    id: 'cs',
    name: 'CS Fundamentals',
    description:
      'OS, computer networks, OOP, and core CS concepts.',
    questionCount: 7
  },

  {
    id: 'hr',
    name: 'HR & Behavioral',
    description:
      'HR, behavioral, communication, and workplace questions.',
    questionCount: 7
  },

  {
    id: 'mock',
    name: 'Mock Interview',
    description:
      'Simulate a complete placement interview.',
    questionCount: 5
  }

]


// ============================================================
// QUESTION BANK
// ============================================================

const interviewQuestions = [

  // ==========================================================
  // TECHNICAL
  // ==========================================================

  {
    id: 'tech-001',
    category: 'Technical Interview',
    topic: 'Java',
    difficulty: 'Easy',
    time: 3,
    question:
      'What are the main features of Java?',
    tags: [
      'Java',
      'OOP'
    ],
    expectation:
      'The interviewer wants to know whether you understand the language fundamentals rather than just memorizing keywords.',
    keyPoints: [
      'Platform independent',
      'Object-oriented',
      'Robust and secure',
      'Automatic memory management',
      'Multithreading support'
    ]
  },


  {
    id: 'tech-002',
    category: 'Technical Interview',
    topic: 'OOP',
    difficulty: 'Easy',
    time: 4,
    question:
      'Explain the four pillars of Object-Oriented Programming.',
    tags: [
      'OOP',
      'Java'
    ],
    expectation:
      'Give a simple definition of each concept and connect it with a practical example.',
    keyPoints: [
      'Encapsulation',
      'Inheritance',
      'Polymorphism',
      'Abstraction'
    ]
  },


  {
    id: 'tech-003',
    category: 'Technical Interview',
    topic: 'Java',
    difficulty: 'Medium',
    time: 5,
    question:
      'What is the difference between an interface and an abstract class in Java?',
    tags: [
      'Java',
      'OOP'
    ],
    expectation:
      'Explain the conceptual difference first, then discuss when you would choose one over the other.',
    keyPoints: [
      'Interfaces define contracts',
      'Abstract classes can contain state and implementation',
      'A class can implement multiple interfaces',
      'A class can extend one class'
    ]
  },


  {
    id: 'tech-004',
    category: 'Technical Interview',
    topic: 'Java',
    difficulty: 'Medium',
    time: 5,
    question:
      'Explain the difference between == and equals() in Java.',
    tags: [
      'Java',
      'Strings'
    ],
    expectation:
      'Clearly distinguish reference comparison from logical/content comparison.',
    keyPoints: [
      '== compares primitive values or references',
      'equals() is used for logical equality',
      'String overrides equals()',
      'Reference comparison and content comparison are different'
    ]
  },


  {
    id: 'tech-005',
    category: 'Technical Interview',
    topic: 'Backend',
    difficulty: 'Medium',
    time: 5,
    question:
      'What is REST API and how does a client communicate with it?',
    tags: [
      'REST',
      'API'
    ],
    expectation:
      'Explain the client-server interaction and common HTTP methods.',
    keyPoints: [
      'Client-server architecture',
      'HTTP requests and responses',
      'GET, POST, PUT, PATCH, DELETE',
      'Stateless communication',
      'JSON is commonly used for data exchange'
    ]
  },


  {
    id: 'tech-006',
    category: 'Technical Interview',
    topic: 'Web',
    difficulty: 'Easy',
    time: 4,
    question:
      'What is the difference between frontend and backend development?',
    tags: [
      'Web',
      'Development'
    ],
    expectation:
      'Show that you understand how the browser, backend server, APIs, and database work together.',
    keyPoints: [
      'Frontend runs in the client/browser',
      'Backend handles server-side logic',
      'APIs connect frontend and backend',
      'Backend commonly communicates with databases'
    ]
  },


  {
    id: 'tech-007',
    category: 'Technical Interview',
    topic: 'Authentication',
    difficulty: 'Medium',
    time: 5,
    question:
      'What is authentication and how is it different from authorization?',
    tags: [
      'Security',
      'Auth'
    ],
    expectation:
      'Give the distinction clearly and provide a simple real-world example.',
    keyPoints: [
      'Authentication verifies identity',
      'Authorization determines permissions',
      'Login is an authentication example',
      'Role-based access is an authorization example'
    ]
  },


  {
    id: 'tech-008',
    category: 'Technical Interview',
    topic: 'Git',
    difficulty: 'Easy',
    time: 4,
    question:
      'What is Git and why is it used in software development?',
    tags: [
      'Git',
      'Version Control'
    ],
    expectation:
      'Explain Git as a version-control system and mention collaboration.',
    keyPoints: [
      'Version control',
      'Track code changes',
      'Branches',
      'Merging',
      'Team collaboration'
    ]
  },


  // ==========================================================
  // DSA
  // ==========================================================

  {
    id: 'dsa-001',
    category: 'DSA Interview',
    topic: 'Arrays',
    difficulty: 'Easy',
    time: 5,
    question:
      'How would you find the largest element in an array?',
    tags: [
      'Arrays',
      'Basics'
    ],
    expectation:
      'Start with the simplest one-pass solution and state its complexity.',
    keyPoints: [
      'Initialize maximum',
      'Traverse the array once',
      'Update maximum when needed',
      'Time complexity O(n)',
      'Space complexity O(1)'
    ]
  },


  {
    id: 'dsa-002',
    category: 'DSA Interview',
    topic: 'HashMap',
    difficulty: 'Easy',
    time: 6,
    question:
      'How would you find the first non-repeating element in an array or string?',
    tags: [
      'HashMap',
      'Frequency'
    ],
    expectation:
      'Explain how frequency counting can avoid repeatedly scanning the entire input.',
    keyPoints: [
      'Count frequencies',
      'Store values in a HashMap',
      'Traverse again to find first frequency one',
      'Average O(n) time',
      'O(n) extra space'
    ]
  },


  {
    id: 'dsa-003',
    category: 'DSA Interview',
    topic: 'Two Pointers',
    difficulty: 'Medium',
    time: 7,
    question:
      'Explain the two-pointer technique and give an example where it is useful.',
    tags: [
      'Two Pointers',
      'Arrays'
    ],
    expectation:
      'Explain the pattern rather than only describing one problem.',
    keyPoints: [
      'Maintain two indices',
      'Move pointers based on a condition',
      'Often works on sorted arrays',
      'Can reduce nested loops',
      'Commonly O(n)'
    ]
  },


  {
    id: 'dsa-004',
    category: 'DSA Interview',
    topic: 'Sliding Window',
    difficulty: 'Medium',
    time: 7,
    question:
      'What is the sliding window technique?',
    tags: [
      'Sliding Window',
      'Arrays'
    ],
    expectation:
      'Explain how a changing window avoids recomputing overlapping ranges.',
    keyPoints: [
      'Maintain a window',
      'Expand the right side',
      'Shrink the left side when required',
      'Useful for contiguous subarrays or substrings',
      'Often reduces O(n²) to O(n)'
    ]
  },


  {
    id: 'dsa-005',
    category: 'DSA Interview',
    topic: 'Binary Search',
    difficulty: 'Medium',
    time: 7,
    question:
      'Explain binary search and its time complexity.',
    tags: [
      'Binary Search',
      'Searching'
    ],
    expectation:
      'Mention the sorted-input requirement and explain how the search space is reduced.',
    keyPoints: [
      'Array should generally be sorted',
      'Check middle element',
      'Discard half of search space',
      'O(log n) time',
      'O(1) iterative space'
    ]
  },


  {
    id: 'dsa-006',
    category: 'DSA Interview',
    topic: 'Linked List',
    difficulty: 'Medium',
    time: 7,
    question:
      'How can you detect a cycle in a linked list?',
    tags: [
      'Linked List',
      'Fast Slow Pointer'
    ],
    expectation: "Explain Floyd's slow and fast pointer technique.",
    keyPoints: [
        "Slow moves one step",
        "Fast moves two steps",
        "If they meet, a cycle exists",
        "O(n) time",
        "O(1) space"
    ]
  },


  {
    id: 'dsa-007',
    category: 'DSA Interview',
    topic: 'Stack',
    difficulty: 'Easy',
    time: 5,
    question:
      'What is a stack and where is it used?',
    tags: [
      'Stack',
      'Data Structures'
    ],
    expectation:
      'Explain LIFO and provide practical programming examples.',
    keyPoints: [
      'LIFO',
      'Push and pop',
      'Function call stack',
      'Undo operations',
      'Parentheses matching'
    ]
  },


  {
    id: 'dsa-008',
    category: 'DSA Interview',
    topic: 'Complexity',
    difficulty: 'Medium',
    time: 6,
    question:
      'How do you analyze the time and space complexity of an algorithm?',
    tags: [
      'Big O',
      'Complexity'
    ],
    expectation:
      'Explain how input size affects the number of operations and additional memory.',
    keyPoints: [
      'Identify input size',
      'Count dominant operations',
      'Ignore constant factors',
      'Consider nested loops',
      'Analyze auxiliary space'
    ]
  },


  // ==========================================================
  // SQL & DBMS
  // ==========================================================

  {
    id: 'sql-001',
    category: 'SQL & DBMS',
    topic: 'SQL',
    difficulty: 'Easy',
    time: 5,
    question:
      'What is the difference between WHERE and HAVING in SQL?',
    tags: [
      'SQL',
      'Queries'
    ],
    expectation:
      'Explain when each clause filters data.',
    keyPoints: [
      'WHERE filters rows',
      'HAVING filters groups',
      'HAVING is commonly used with GROUP BY',
      'WHERE generally occurs before grouping'
    ]
  },


  {
    id: 'sql-002',
    category: 'SQL & DBMS',
    topic: 'Joins',
    difficulty: 'Medium',
    time: 7,
    question:
      'Explain INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.',
    tags: [
      'SQL',
      'Joins'
    ],
    expectation:
      'Describe what happens to matching and non-matching rows.',
    keyPoints: [
      'INNER JOIN returns matching rows',
      'LEFT JOIN keeps all left rows',
      'RIGHT JOIN keeps all right rows',
      'FULL JOIN keeps rows from both sides'
    ]
  },


  {
    id: 'sql-003',
    category: 'SQL & DBMS',
    topic: 'Normalization',
    difficulty: 'Medium',
    time: 6,
    question:
      'What is database normalization and why is it used?',
    tags: [
      'DBMS',
      'Normalization'
    ],
    expectation:
      'Explain normalization as a way to reduce redundancy and improve data consistency.',
    keyPoints: [
      'Reduce data redundancy',
      'Avoid update anomalies',
      'Improve consistency',
      '1NF, 2NF, 3NF',
      'Decomposition of tables'
    ]
  },


  {
    id: 'sql-004',
    category: 'SQL & DBMS',
    topic: 'Keys',
    difficulty: 'Easy',
    time: 5,
    question:
      'What are primary key, foreign key, candidate key, and composite key?',
    tags: [
      'DBMS',
      'Keys'
    ],
    expectation:
      'Define each key and explain its role in maintaining data integrity.',
    keyPoints: [
      'Primary key uniquely identifies rows',
      'Foreign key establishes relationships',
      'Candidate keys can uniquely identify rows',
      'Composite key uses multiple columns'
    ]
  },


  {
    id: 'sql-005',
    category: 'SQL & DBMS',
    topic: 'Transactions',
    difficulty: 'Medium',
    time: 6,
    question:
      'What are ACID properties in database transactions?',
    tags: [
      'DBMS',
      'Transactions'
    ],
    expectation:
      'Explain all four properties with a transaction example.',
    keyPoints: [
      'Atomicity',
      'Consistency',
      'Isolation',
      'Durability'
    ]
  },


  {
    id: 'sql-006',
    category: 'SQL & DBMS',
    topic: 'Indexes',
    difficulty: 'Medium',
    time: 5,
    question:
      'What is a database index and what are its advantages and disadvantages?',
    tags: [
      'DBMS',
      'Index'
    ],
    expectation:
      'Explain the performance trade-off rather than saying indexes are always good.',
    keyPoints: [
      'Speeds up data retrieval',
      'Uses additional storage',
      'Can slow writes',
      'Useful on frequently searched columns'
    ]
  },


  {
    id: 'sql-007',
    category: 'SQL & DBMS',
    topic: 'SQL',
    difficulty: 'Hard',
    time: 8,
    question:
      'How would you find the second highest salary from an employee table?',
    tags: [
      'SQL',
      'Subquery'
    ],
    expectation:
      'Discuss at least one correct SQL approach and handle duplicate salaries appropriately.',
    keyPoints: [
      'DISTINCT can matter',
      'ORDER BY with LIMIT',
      'Subquery approach',
      'DENSE_RANK approach',
      'Consider duplicate salaries'
    ]
  },


  // ==========================================================
  // CS FUNDAMENTALS
  // ==========================================================

  {
    id: 'cs-001',
    category: 'CS Fundamentals',
    topic: 'Operating Systems',
    difficulty: 'Easy',
    time: 5,
    question:
      'What is the difference between a process and a thread?',
    tags: [
      'OS',
      'Threads'
    ],
    expectation:
      'Explain memory isolation and resource sharing.',
    keyPoints: [
      'Process is an independent execution unit',
      'Threads exist inside processes',
      'Threads share process memory',
      'Processes have greater isolation',
      'Threads are generally lighter'
    ]
  },


  {
    id: 'cs-002',
    category: 'CS Fundamentals',
    topic: 'Operating Systems',
    difficulty: 'Medium',
    time: 6,
    question:
      'What is deadlock in an operating system?',
    tags: [
      'OS',
      'Deadlock'
    ],
    expectation:
      'Define deadlock and mention its necessary conditions.',
    keyPoints: [
      'Processes wait indefinitely',
      'Mutual exclusion',
      'Hold and wait',
      'No preemption',
      'Circular wait'
    ]
  },


  {
    id: 'cs-003',
    category: 'CS Fundamentals',
    topic: 'Computer Networks',
    difficulty: 'Easy',
    time: 5,
    question:
      'What is the difference between HTTP and HTTPS?',
    tags: [
      'Networking',
      'Security'
    ],
    expectation:
      'Explain the security layer provided by HTTPS.',
    keyPoints: [
      'HTTPS uses TLS',
      'Encrypts communication',
      'Provides server authentication',
      'Protects data in transit'
    ]
  },


  {
    id: 'cs-004',
    category: 'CS Fundamentals',
    topic: 'Networking',
    difficulty: 'Medium',
    time: 6,
    question:
      'What happens when you enter a URL into a browser?',
    tags: [
      'Networking',
      'Web'
    ],
    expectation:
      'Walk through DNS, connection establishment, HTTP request, server response, and rendering at a high level.',
    keyPoints: [
      'DNS resolution',
      'Connection establishment',
      'HTTP request',
      'Server response',
      'Browser rendering'
    ]
  },


  {
    id: 'cs-005',
    category: 'CS Fundamentals',
    topic: 'DBMS',
    difficulty: 'Easy',
    time: 5,
    question:
      'What is a database management system?',
    tags: [
      'DBMS',
      'Database'
    ],
    expectation:
      'Explain why DBMS software is used instead of managing raw data files manually.',
    keyPoints: [
      'Stores and manages data',
      'Provides querying',
      'Security',
      'Concurrency',
      'Backup and recovery'
    ]
  },


  {
    id: 'cs-006',
    category: 'CS Fundamentals',
    topic: 'OOP',
    difficulty: 'Easy',
    time: 5,
    question:
      'What is polymorphism? Explain compile-time and runtime polymorphism.',
    tags: [
      'OOP',
      'Java'
    ],
    expectation:
      'Use method overloading and overriding as the standard examples.',
    keyPoints: [
      'One interface, multiple behaviors',
      'Method overloading',
      'Method overriding',
      'Compile-time resolution',
      'Runtime dispatch'
    ]
  },


  {
    id: 'cs-007',
    category: 'CS Fundamentals',
    topic: 'Operating Systems',
    difficulty: 'Medium',
    time: 6,
    question:
      'What is virtual memory?',
    tags: [
      'OS',
      'Memory'
    ],
    expectation:
      'Explain how the operating system provides the illusion of a larger memory space.',
    keyPoints: [
      'Uses secondary storage',
      'Allows processes to use virtual addresses',
      'Paging is commonly used',
      'Provides process isolation',
      'Can cause performance overhead'
    ]
  },


  // ==========================================================
  // HR & BEHAVIORAL
  // ==========================================================

  {
    id: 'hr-001',
    category: 'HR & Behavioral',
    topic: 'Introduction',
    difficulty: 'Easy',
    time: 3,
    question:
      'Tell me about yourself.',
    tags: [
      'HR',
      'Introduction'
    ],
    expectation:
      'Give a concise professional introduction focused on education, relevant skills, projects, and career direction.',
    keyPoints: [
      'Education',
      'Technical skills',
      'Projects or experience',
      'Relevant strengths',
      'Career goal'
    ]
  },


  {
    id: 'hr-002',
    category: 'HR & Behavioral',
    topic: 'Projects',
    difficulty: 'Easy',
    time: 5,
    question:
      'Tell me about a project you are proud of.',
    tags: [
      'HR',
      'Projects'
    ],
    expectation:
      'Explain the problem, your role, technology used, challenges, and result.',
    keyPoints: [
      'Problem statement',
      'Your contribution',
      'Technology stack',
      'Challenge',
      'Outcome'
    ]
  },


  {
    id: 'hr-003',
    category: 'HR & Behavioral',
    topic: 'Behavioral',
    difficulty: 'Medium',
    time: 5,
    question:
      'Tell me about a challenge you faced and how you handled it.',
    tags: [
      'HR',
      'STAR'
    ],
    expectation:
      'Use a structured story instead of giving a vague answer.',
    keyPoints: [
      'Situation',
      'Task',
      'Action',
      'Result',
      'What you learned'
    ]
  },


  {
    id: 'hr-004',
    category: 'HR & Behavioral',
    topic: 'Strengths',
    difficulty: 'Easy',
    time: 4,
    question:
      'What are your strengths?',
    tags: [
      'HR',
      'Behavioral'
    ],
    expectation:
      'Mention strengths that are relevant to the role and support them with examples.',
    keyPoints: [
      'Choose relevant strengths',
      'Give evidence',
      'Avoid generic claims',
      'Connect strengths to the role'
    ]
  },


  {
    id: 'hr-005',
    category: 'HR & Behavioral',
    topic: 'Weaknesses',
    difficulty: 'Medium',
    time: 4,
    question:
      'What is one weakness you are currently working on?',
    tags: [
      'HR',
      'Behavioral'
    ],
    expectation:
      'Choose a genuine but manageable weakness and explain what you are doing to improve it.',
    keyPoints: [
      'Be honest',
      'Avoid role-critical weaknesses',
      'Explain improvement steps',
      'Show progress'
    ]
  },


  {
    id: 'hr-006',
    category: 'HR & Behavioral',
    topic: 'Career',
    difficulty: 'Easy',
    time: 4,
    question:
      'Where do you see yourself in five years?',
    tags: [
      'HR',
      'Career'
    ],
    expectation:
      'Show realistic career growth while demonstrating alignment with the company and role.',
    keyPoints: [
      'Professional growth',
      'Skill development',
      'Increasing responsibility',
      'Role alignment'
    ]
  },


  {
    id: 'hr-007',
    category: 'HR & Behavioral',
    topic: 'Company',
    difficulty: 'Medium',
    time: 5,
    question:
      'Why should we hire you?',
    tags: [
      'HR',
      'Behavioral'
    ],
    expectation:
      'Connect your skills, projects, learning ability, and role fit to the company’s needs.',
    keyPoints: [
      'Relevant skills',
      'Evidence from projects',
      'Learning ability',
      'Problem-solving mindset',
      'Role fit'
    ]
  }

]


// ============================================================
// INTERVIEW STATS
// ============================================================
//
// These are intentionally mock values for the frontend.
//
// Later they can come from:
// GET /api/interview-prep/stats
//
// ============================================================

const interviewStats = {

  questionsPracticed: 0,

  accuracy: 0,

  streak: 0,

  mockInterviews: 0

}


// ============================================================
// GET CATEGORIES
// ============================================================

export async function getInterviewCategories() {

  await simulateDelay(250)

  return interviewCategories

}


// ============================================================
// GET QUESTIONS
// ============================================================

export async function getInterviewQuestions() {

  await simulateDelay(350)

  return interviewQuestions

}


// ============================================================
// GET STATS
// ============================================================

export async function getInterviewStats() {

  await simulateDelay(200)

  return interviewStats

}


// ============================================================
// GET MOCK INTERVIEW QUESTIONS
// ============================================================
//
// Later:
// This function will call the Interview Agent.
//
// Example future endpoint:
//
// POST /api/interview-prep/mock/start
//
// ============================================================

export async function getMockInterviewQuestions({

  role = 'Software Developer',

  difficulty = 'Mixed',

  count = 5

} = {}) {

  await simulateDelay(500)


  let pool =
    [...interviewQuestions]


  // ----------------------------------------------------------
  // Filter by difficulty when requested.
  // ----------------------------------------------------------

  if (
    difficulty !== 'Mixed'
  ) {

    const filtered =
      pool.filter(
        (question) =>
          question.difficulty ===
          difficulty
      )


    if (filtered.length >= count) {

      pool = filtered

    }

  }


  // ----------------------------------------------------------
  // Shuffle locally.
  // ----------------------------------------------------------

  pool =
    pool.sort(
      () => Math.random() - 0.5
    )


  // ----------------------------------------------------------
  // Select questions.
  // ----------------------------------------------------------

  const selected =
    pool.slice(0, count)


  return selected.map(
    (question) => ({

      ...question,

      role

    })
  )

}


// ============================================================
// UTILITY
// ============================================================

function simulateDelay(milliseconds) {

  return new Promise(
    (resolve) => {

      setTimeout(
        resolve,
        milliseconds
      )

    }
  )

}


// ============================================================
// FUTURE FASTAPI EXAMPLE
// ============================================================
//
// const response = await fetch(
//   `${API_BASE_URL}/api/interview-prep/questions`,
//   {
//     method: 'GET'
//   }
// )
//
// const data = await response.json()
//
// return data.questions
//
// ============================================================
//
// FUTURE MOCK INTERVIEW:
//
// const response = await fetch(
//   `${API_BASE_URL}/api/interview-prep/mock/start`,
//   {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//       role,
//       difficulty,
//       count
//     })
//   }
// )
//
// const data = await response.json()
//
// return data.questions
//
// ============================================================
//
// FUTURE AI EVALUATION:
//
// const response = await fetch(
//   `${API_BASE_URL}/api/interview-prep/evaluate`,
//   {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//       role,
//       question,
//       answer,
//       conversation
//     })
//   }
// )
//
// const data = await response.json()
//
// return data
//
// ============================================================