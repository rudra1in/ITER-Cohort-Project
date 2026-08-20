const fs = require("fs");
const path = require("path");

// ============================================================
// CONFIGURATION
// ============================================================

const TOPIC = "sliding_window";

const outputDir = path.join(
  __dirname,
  "data",
  "dsa",
  TOPIC
);

// ============================================================
// PROBLEMS
// ============================================================

const problems = [

  // ==========================================================
  // 1. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
  // ==========================================================

  {
    id: "longest_substring_without_repeating_characters",
    name: "Longest Substring Without Repeating Characters",
    difficulty: "Medium",
    pattern: "Variable Sliding Window",
    slug: "longest_substring_without_repeating_characters",

    keyIdea:
      "Maintain a sliding window containing unique characters. Expand the right pointer and move the left pointer whenever a duplicate character appears.",

    bruteForce:
      "Generate every possible substring and check whether all characters are unique.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Initialize left = 0 and a frequency map or set.",
      "Move the right pointer through the string.",
      "Add the current character to the window.",
      "If the character already exists in the window, move left forward until the window becomes valid.",
      "Track the maximum window length."
    ],

    invariant:
      "The current window always contains no duplicate characters.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(K), where K is the number of distinct characters.",

    hints: [
      "Can you maintain a window containing only unique characters?",
      "What should happen when a duplicate character enters the window?",
      "Can a HashSet or frequency array help?"
    ],

    commonMistakes: [
      "Not moving the left pointer when a duplicate appears.",
      "Moving left only once instead of until the window becomes valid.",
      "Updating the maximum length before restoring the valid window.",
      "Using O(N^2) substring generation unnecessarily."
    ],

    edgeCases: [
      "Empty string.",
      "String with one character.",
      "All characters are unique.",
      "All characters are identical.",
      "Duplicate occurs immediately.",
      "Duplicate occurs near the end."
    ],

    keywords: [
      "sliding window",
      "longest substring",
      "no repeating characters",
      "HashSet",
      "frequency map",
      "variable window"
    ]
  },


  // ==========================================================
  // 2. MAX CONSECUTIVE ONES III
  // ==========================================================

  {
    id: "max_consecutive_ones_iii",
    name: "Max Consecutive Ones III",
    difficulty: "Medium",
    pattern: "Variable Sliding Window",
    slug: "max_consecutive_ones_iii",

    keyIdea:
      "Maintain a window containing at most K zeros. Zeros inside the window can be flipped to ones, so the largest valid window gives the answer.",

    bruteForce:
      "Generate every subarray and count the number of zeros. Keep the longest subarray containing at most K zeros.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Initialize left = 0 and zeroCount = 0.",
      "Expand the right pointer.",
      "If nums[right] is zero, increment zeroCount.",
      "If zeroCount becomes greater than K, move left forward and remove zeros from the window.",
      "Track the maximum valid window length."
    ],

    invariant:
      "The current window contains at most K zeros.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "What does K represent?",
      "Can you allow at most K zeros inside the current window?",
      "When should the left pointer move?"
    ],

    commonMistakes: [
      "Allowing more than K zeros.",
      "Forgetting to decrease zeroCount when moving left.",
      "Using nested loops unnecessarily.",
      "Confusing K zeros with K ones."
    ],

    edgeCases: [
      "K equals 0.",
      "K is greater than the number of zeros.",
      "Array contains only zeros.",
      "Array contains only ones.",
      "Single-element array."
    ],

    keywords: [
      "sliding window",
      "maximum consecutive ones",
      "K zeros",
      "variable window",
      "two pointers"
    ]
  },


  // ==========================================================
  // 3. FRUIT INTO BASKETS
  // ==========================================================

  {
    id: "fruit_into_baskets",
    name: "Fruit Into Baskets",
    difficulty: "Medium",
    pattern: "At Most 2 Distinct Sliding Window",
    slug: "fruit_into_baskets",

    keyIdea:
      "Find the longest contiguous subarray containing at most two distinct fruit types.",

    bruteForce:
      "Generate every subarray and count the number of distinct fruit types.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Initialize left = 0 and a frequency map.",
      "Expand the right pointer.",
      "Add fruits[right] to the frequency map.",
      "If the number of distinct fruit types becomes greater than 2, move left forward.",
      "Remove elements from the frequency map as they leave the window.",
      "Track the maximum window length."
    ],

    invariant:
      "The current window contains at most two distinct fruit types.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "How many distinct fruit types can the window contain?",
      "What data structure can count distinct values?",
      "When should the left pointer move?"
    ],

    commonMistakes: [
      "Allowing three fruit types in the window.",
      "Forgetting to remove a fruit when its frequency becomes zero.",
      "Counting total fruits instead of distinct types.",
      "Resetting the entire window unnecessarily."
    ],

    edgeCases: [
      "Empty array.",
      "One fruit type.",
      "Exactly two fruit types.",
      "Every fruit is different.",
      "All fruits are identical."
    ],

    keywords: [
      "fruit into baskets",
      "at most two distinct",
      "sliding window",
      "frequency map",
      "variable window"
    ]
  },


  // ==========================================================
  // 4. LONGEST REPEATING CHARACTER REPLACEMENT
  // ==========================================================

  {
    id: "longest_repeating_character_replacement",
    name: "Longest Repeating Character Replacement",
    difficulty: "Medium",
    pattern: "Frequency + Variable Sliding Window",
    slug: "longest_repeating_character_replacement",

    keyIdea:
      "Maintain a window where the number of characters that must be replaced is at most K. The number of replacements needed is window length minus the frequency of the most frequent character.",

    bruteForce:
      "Generate every substring and determine how many characters need to be replaced to make all characters equal.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Initialize left = 0 and a frequency array.",
      "Expand the right pointer.",
      "Update the frequency of the current character.",
      "Track the highest frequency inside the window.",
      "Calculate replacements as windowLength - maxFrequency.",
      "If replacements exceed K, move left forward.",
      "Track the largest valid window."
    ],

    invariant:
      "The current window can be converted into a string of identical characters using at most K replacements.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "Which character should remain unchanged?",
      "How many characters need replacement?",
      "Can windowLength - maxFrequency tell you the required replacements?"
    ],

    commonMistakes: [
      "Using the total frequency instead of maximum frequency.",
      "Shrinking the window at the wrong condition.",
      "Forgetting to update the maximum frequency.",
      "Recomputing all character frequencies for every window."
    ],

    edgeCases: [
      "K equals 0.",
      "K is greater than or equal to string length.",
      "All characters are identical.",
      "All characters are different.",
      "Single-character string."
    ],

    keywords: [
      "character replacement",
      "sliding window",
      "frequency",
      "maximum frequency",
      "K replacements"
    ]
  },


  // ==========================================================
  // 5. BINARY SUBARRAYS WITH SUM
  // ==========================================================

  {
    id: "binary_subarrays_with_sum",
    name: "Binary Subarrays With Sum",
    difficulty: "Medium",
    pattern: "AtMost Sliding Window",
    slug: "binary_subarrays_with_sum",

    keyIdea:
      "For a binary array, count subarrays with sum exactly goal using atMost(goal) - atMost(goal - 1).",

    bruteForce:
      "Generate every subarray and calculate its sum. Count subarrays whose sum equals the target.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Create a helper function atMost(goal).",
      "Maintain a sliding window whose sum is at most goal.",
      "Expand the right pointer and add nums[right].",
      "While the sum is greater than goal, move left forward.",
      "Every valid window ending at right contributes right - left + 1 subarrays.",
      "Return atMost(goal) - atMost(goal - 1)."
    ],

    invariant:
      "The sliding window maintained by atMost contains a sum less than or equal to the specified goal.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "Can you count subarrays with sum at most goal?",
      "How can exactly goal be obtained from two atMost counts?",
      "Why does right - left + 1 count valid subarrays?"
    ],

    commonMistakes: [
      "Trying to directly count exact sums using a normal shrinking window.",
      "Forgetting the atMost(goal - 1) term.",
      "Not handling goal = 0 correctly.",
      "Using this exact technique on arbitrary negative numbers."
    ],

    edgeCases: [
      "Goal equals 0.",
      "All elements are zero.",
      "All elements are one.",
      "Single-element array.",
      "Goal is larger than total sum."
    ],

    keywords: [
      "binary subarray",
      "exact sum",
      "at most",
      "sliding window",
      "prefix sum alternative"
    ]
  },


  // ==========================================================
  // 6. COUNT NUMBER OF NICE SUBARRAYS
  // ==========================================================

  {
    id: "count_number_of_nice_subarrays",
    name: "Count Number of Nice Subarrays",
    difficulty: "Medium",
    pattern: "AtMost Sliding Window",
    slug: "count_number_of_nice_subarrays",

    keyIdea:
      "A nice subarray contains exactly K odd numbers. Count subarrays with at most K odd numbers and subtract those with at most K - 1 odd numbers.",

    bruteForce:
      "Generate every subarray and count the number of odd elements.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Create a helper function that counts subarrays with at most K odd numbers.",
      "Maintain a sliding window.",
      "Increment oddCount whenever an odd number enters.",
      "If oddCount exceeds K, move left forward.",
      "Add right - left + 1 to the answer.",
      "Return atMost(K) - atMost(K - 1)."
    ],

    invariant:
      "The current window contains at most K odd numbers.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "What property makes a subarray nice?",
      "Can you convert exactly K into two atMost problems?",
      "How do you count valid subarrays ending at right?"
    ],

    commonMistakes: [
      "Counting exactly K directly with an incorrect shrinking rule.",
      "Forgetting K - 1.",
      "Checking even numbers instead of odd numbers.",
      "Incorrectly counting valid windows."
    ],

    edgeCases: [
      "K equals 0 if allowed.",
      "K equals 1.",
      "No odd numbers.",
      "All numbers are odd.",
      "K is greater than the number of odd elements."
    ],

    keywords: [
      "nice subarrays",
      "exactly K odd",
      "at most K",
      "sliding window",
      "two pointers"
    ]
  },


  // ==========================================================
  // 7. NUMBER OF SUBSTRINGS CONTAINING ALL THREE CHARACTERS
  // ==========================================================

  {
    id: "number_of_substrings_containing_all_three_characters",
    name: "Number of Substrings Containing All Three Characters",
    difficulty: "Medium",
    pattern: "Frequency + Sliding Window",
    slug: "number_of_substrings_containing_all_three_characters",

    keyIdea:
      "Maintain a window containing characters a, b, and c. Once the window contains all three characters, every extension to the right remains valid.",

    bruteForce:
      "Generate every substring and check whether it contains a, b, and c.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Maintain the last occurrence or frequency of a, b, and c.",
      "Move the right pointer through the string.",
      "Update the position or frequency of the current character.",
      "When all three characters have appeared, count all valid starting positions.",
      "Continue expanding the right pointer."
    ],

    invariant:
      "Whenever the window contains all three required characters, the counted substrings satisfy the requirement.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "What are the required characters?",
      "Can you track their latest positions?",
      "If the current window contains all three, how many starting positions can be valid?"
    ],

    commonMistakes: [
      "Counting only the current window.",
      "Forgetting that extending the substring to the right preserves validity.",
      "Using O(N^2) substring creation.",
      "Incorrectly handling the first occurrence of each character."
    ],

    edgeCases: [
      "String shorter than three characters.",
      "Only one distinct character.",
      "Exactly one occurrence of each character.",
      "Repeated characters.",
      "All three characters appear near the end."
    ],

    keywords: [
      "substrings",
      "all three characters",
      "a b c",
      "sliding window",
      "frequency",
      "last occurrence"
    ]
  },


  // ==========================================================
  // 8. MAXIMUM POINTS YOU CAN OBTAIN FROM CARDS
  // ==========================================================

  {
    id: "maximum_points_you_can_obtain_from_cards",
    name: "Maximum Points You Can Obtain from Cards",
    difficulty: "Medium",
    pattern: "Fixed Sliding Window / Complement",
    slug: "maximum_points_you_can_obtain_from_cards",

    keyIdea:
      "Instead of choosing K cards from the ends directly, find the minimum-sum subarray of length N-K that must remain in the middle. Subtract that minimum sum from the total.",

    bruteForce:
      "Try every possible combination of taking cards from the left and right ends.",

    bruteForceComplexity: "O(K)",

    optimizedSteps: [
      "Calculate the total sum of all cards.",
      "The number of cards left in the middle is N - K.",
      "Find the minimum-sum contiguous subarray of length N - K.",
      "Subtract that minimum sum from the total sum.",
      "The remaining sum is the maximum score obtainable."
    ],

    invariant:
      "The fixed-size window represents the cards that are not selected.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "If you take K cards, how many cards remain?",
      "Can the unselected cards form one contiguous middle segment?",
      "Would maximizing selected sum be equivalent to minimizing the middle segment?"
    ],

    commonMistakes: [
      "Trying all left/right combinations unnecessarily.",
      "Using the maximum window instead of the minimum window.",
      "Using the wrong window length N - K.",
      "Forgetting to handle K = N."
    ],

    edgeCases: [
      "K equals 0.",
      "K equals N.",
      "K equals 1.",
      "All card values are equal.",
      "Single-card array."
    ],

    keywords: [
      "maximum points",
      "cards",
      "fixed window",
      "complement window",
      "minimum sum subarray"
    ]
  },


  // ==========================================================
  // 9. LONGEST SUBSTRING WITH AT MOST K DISTINCT CHARACTERS
  // ==========================================================

  {
    id: "longest_substring_with_at_most_k_distinct_characters",
    name: "Longest Substring With At Most K Distinct Characters",
    difficulty: "Medium",
    pattern: "At Most K Distinct Sliding Window",
    slug: "longest_substring_with_at_most_k_distinct_characters",

    keyIdea:
      "Maintain a window containing at most K distinct characters and maximize its length.",

    bruteForce:
      "Generate every substring and count the number of distinct characters.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Initialize left = 0 and a frequency map.",
      "Expand the right pointer.",
      "Add the current character to the frequency map.",
      "If the number of distinct characters exceeds K, move left forward.",
      "Remove characters whose frequency becomes zero.",
      "Track the maximum window length."
    ],

    invariant:
      "The current window always contains at most K distinct characters.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(K)",

    hints: [
      "What exactly does K limit?",
      "How can a frequency map track distinct characters?",
      "When should the window shrink?"
    ],

    commonMistakes: [
      "Counting character frequency instead of distinct characters.",
      "Not deleting characters when their frequency reaches zero.",
      "Allowing K + 1 distinct characters.",
      "Using nested loops unnecessarily."
    ],

    edgeCases: [
      "K equals 0.",
      "K equals 1.",
      "K is greater than the number of distinct characters.",
      "Empty string.",
      "All characters are identical."
    ],

    keywords: [
      "at most K distinct",
      "longest substring",
      "sliding window",
      "frequency map",
      "variable window"
    ]
  },


  // ==========================================================
  // 10. SUBARRAYS WITH K DIFFERENT INTEGERS
  // ==========================================================

  {
    id: "subarrays_with_k_different_integers",
    name: "Subarrays with K Different Integers",
    difficulty: "Hard",
    pattern: "AtMost(K) - AtMost(K-1)",
    slug: "subarrays_with_k_different_integers",

    keyIdea:
      "Count subarrays with exactly K distinct integers by calculating atMost(K) - atMost(K - 1).",

    bruteForce:
      "Generate every subarray and count its distinct integers.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Create a helper function that counts subarrays with at most K distinct integers.",
      "Maintain a frequency map for the current window.",
      "Expand the right pointer.",
      "If the number of distinct integers exceeds K, move left forward.",
      "Add right - left + 1 to the count.",
      "Return atMost(K) - atMost(K - 1)."
    ],

    invariant:
      "The helper window contains at most K distinct integers.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(K)",

    hints: [
      "Can exactly K be expressed using two atMost calculations?",
      "How do you maintain distinct integer count?",
      "Why are right - left + 1 subarrays valid?"
    ],

    commonMistakes: [
      "Trying to count exactly K directly.",
      "Forgetting the atMost(K - 1) subtraction.",
      "Not deleting zero-frequency elements.",
      "Counting frequencies instead of distinct values."
    ],

    edgeCases: [
      "K equals 1.",
      "K equals number of distinct values.",
      "All elements are identical.",
      "All elements are different.",
      "K is greater than the number of distinct elements."
    ],

    keywords: [
      "subarrays with K distinct",
      "exactly K",
      "at most K",
      "frequency map",
      "sliding window"
    ]
  },


  // ==========================================================
  // 11. MINIMUM WINDOW SUBSTRING
  // ==========================================================

  {
    id: "minimum_window_substring",
    name: "Minimum Window Substring",
    difficulty: "Hard",
    pattern: "Required Frequency + Variable Sliding Window",
    slug: "minimum_window_substring",

    keyIdea:
      "Find the smallest substring of s that contains all characters of t with the required frequencies. Expand until valid, then shrink from the left while validity is maintained.",

    bruteForce:
      "Generate every substring of s and check whether it contains all required characters with sufficient frequency.",

    bruteForceComplexity: "O(N^2 * K)",

    optimizedSteps: [
      "Build a frequency map for the required characters in t.",
      "Initialize left = 0 and track how many required characters are satisfied.",
      "Expand the right pointer and update the window frequency.",
      "When the window satisfies all required frequencies, record its length.",
      "Move left forward to make the window as small as possible.",
      "Stop shrinking when the window becomes invalid.",
      "Continue expanding right until the entire string is processed."
    ],

    invariant:
      "Whenever the window is considered valid, it contains every required character with at least the required frequency.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(K)",

    hints: [
      "How can you track required frequencies?",
      "When is the current window valid?",
      "Once valid, should you expand or shrink?",
      "Can every character enter and leave the window at most once?"
    ],

    commonMistakes: [
      "Checking only whether characters exist instead of checking frequencies.",
      "Not shrinking the window after it becomes valid.",
      "Updating the answer after the window becomes invalid.",
      "Incorrectly handling duplicate characters in t.",
      "Returning an invalid window when no solution exists."
    ],

    edgeCases: [
      "t is longer than s.",
      "No valid window exists.",
      "s equals t.",
      "t contains duplicate characters.",
      "Multiple valid windows have the same size.",
      "Single-character strings."
    ],

    keywords: [
      "minimum window substring",
      "required frequency",
      "sliding window",
      "HashMap",
      "variable window",
      "frequency matching"
    ]
  },


  // ==========================================================
  // 12. MINIMUM SIZE SUBARRAY SUM
  // ==========================================================

  {
    id: "minimum_size_subarray_sum",
    name: "Minimum Size Subarray Sum",
    difficulty: "Medium",
    pattern: "Variable Sliding Window",
    slug: "minimum_size_subarray_sum",

    keyIdea:
      "For an array of positive integers, expand the window until its sum reaches the target, then shrink it from the left to find the smallest valid window.",

    bruteForce:
      "Generate every subarray and calculate its sum. Track the shortest subarray whose sum is at least the target.",

    bruteForceComplexity: "O(N^2)",

    optimizedSteps: [
      "Initialize left = 0, currentSum = 0, and minimumLength = infinity.",
      "Expand the right pointer and add nums[right] to currentSum.",
      "While currentSum is at least target, update the minimum length.",
      "Remove nums[left] from currentSum and move left forward.",
      "Continue until the right pointer reaches the end.",
      "If no valid subarray exists, return 0."
    ],

    invariant:
      "The current window is adjusted so that when its sum reaches the target, shrinking from the left finds the smallest valid window ending at right.",

    optimizedComplexity: "O(N)",

    spaceComplexity: "O(1)",

    hints: [
      "Why does positivity of the array matter?",
      "When should you expand the window?",
      "When should you shrink it?",
      "Can a valid window become invalid only by removing elements from the left?"
    ],

    commonMistakes: [
      "Using this sliding window approach when negative numbers are present.",
      "Shrinking only once instead of while the sum is valid.",
      "Forgetting to update the answer before shrinking.",
      "Returning infinity instead of 0 when no valid subarray exists."
    ],

    edgeCases: [
      "No subarray reaches the target.",
      "One element equals the target.",
      "The entire array is required.",
      "Target is smaller than the first element.",
      "Single-element array."
    ],

    keywords: [
      "minimum size subarray",
      "minimum length",
      "target sum",
      "positive integers",
      "variable sliding window"
    ]
  }

];


// ============================================================
// ADD TOPIC TO EVERY PROBLEM
// ============================================================

for (const problem of problems) {
  problem.topic = TOPIC;
}


// ============================================================
// VALIDATION
// ============================================================

function validateProblem(problem) {

  const requiredFields = [
    "id",
    "name",
    "difficulty",
    "topic",
    "pattern",
    "slug",
    "keyIdea",
    "bruteForce",
    "bruteForceComplexity",
    "optimizedSteps",
    "invariant",
    "optimizedComplexity",
    "spaceComplexity",
    "hints",
    "commonMistakes",
    "edgeCases",
    "keywords"
  ];

  for (const field of requiredFields) {

    if (
      problem[field] === undefined ||
      problem[field] === null
    ) {
      console.warn(
        `Missing field "${field}" in problem: ${problem.name}`
      );

      return false;
    }
  }

  return true;
}


// ============================================================
// DUPLICATE CHECK
// ============================================================

function checkDuplicateProblems() {

  const seenIds = new Set();
  const seenSlugs = new Set();

  for (const problem of problems) {

    if (seenIds.has(problem.id)) {
      console.warn(
        `Duplicate ID found: ${problem.id}`
      );
    }

    if (seenSlugs.has(problem.slug)) {
      console.warn(
        `Duplicate slug found: ${problem.slug}`
      );
    }

    seenIds.add(problem.id);
    seenSlugs.add(problem.slug);
  }
}


// ============================================================
// MARKDOWN HELPERS
// ============================================================

function formatBulletList(items) {

  return items
    .map(item => `- ${item}`)
    .join("\n");
}


function formatNumberedList(items) {

  return items
    .map((item, index) => `${index + 1}. ${item}`)
    .join("\n");
}


function formatKeywords(keywords) {

  return keywords
    .map(keyword => `- ${keyword}`)
    .join("\n");
}


// ============================================================
// MARKDOWN GENERATOR
// ============================================================

function generateMarkdown(problem) {

  return `# ${problem.name}

Problem ID: ${problem.slug}

Title: ${problem.name}

Difficulty: ${problem.difficulty}

Topic: ${problem.topic}

Pattern: **${problem.pattern}**

---

## Problem Identity

This document is specifically about:

**${problem.name}**

This knowledge chunk belongs to:

**${problem.topic}**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **${problem.name}** problem.

The primary problem-solving pattern is:

**${problem.pattern}**

---

## Key Idea

${problem.keyIdea}

### Core Invariant

${problem.invariant}

---

## Brute Force Approach

${problem.bruteForce}

### Brute Force Complexity

- **Time Complexity:** ${problem.bruteForceComplexity}
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

${formatNumberedList(problem.optimizedSteps)}

### Why This Works

The optimized solution works because it exploits the structure provided by:

**${problem.pattern}**

The algorithm maintains the necessary information while avoiding unnecessary work and ensures that the required answer is preserved throughout the process.

---

## Hints

### Hint 1

${problem.hints[0]}

### Hint 2

${problem.hints[1]}

---

## Common Mistakes

${formatBulletList(problem.commonMistakes)}

---

## Edge Cases

${formatBulletList(problem.edgeCases)}

---

## Complexity Analysis

### Time Complexity

**${problem.optimizedComplexity}**

### Space Complexity

**${problem.spaceComplexity}**

---

## Interview Explanation

A concise interview explanation for **${problem.name}** is:

> ${problem.keyIdea}

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

${formatKeywords(problem.keywords)}

---

## Problem Retrieval Identity

Problem Name: ${problem.name}

Problem ID: ${problem.slug}

Topic: ${problem.topic}

Pattern: ${problem.pattern}

Difficulty: ${problem.difficulty}

Primary Retrieval Entity:

**${problem.name}**

This document should be preferred when a user explicitly asks about:

${formatBulletList(problem.keywords)}

Related concepts:

${formatKeywords(problem.keywords)}
`;
}


// ============================================================
// CLEAN BINARY SEARCH DIRECTORY
// ============================================================

function cleanOutputDirectory() {

  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const files = fs.readdirSync(outputDir);

  for (const file of files) {

    if (!file.endsWith(".md")) {
      continue;
    }

    const filePath = path.join(
      outputDir,
      file
    );

    fs.unlinkSync(filePath);
  }

  console.log(
    `Cleaned existing Markdown files from: ${outputDir}`
  );
}


// ============================================================
// GENERATE FILES
// ============================================================

function generateFiles() {

  console.log(
    "\n=============================================="
  );

  console.log(
    "SLIDING WINDOW DSA MARKDOWN GENERATOR"
  );

  console.log(
    "==============================================\n"
  );

  console.log(
    `Problems in source array: ${problems.length}`
  );

  checkDuplicateProblems();

  cleanOutputDirectory();

  let generated = 0;
  let skipped = 0;

  for (const problem of problems) {

    if (!validateProblem(problem)) {

      skipped++;

      continue;
    }

    const filePath = path.join(
      outputDir,
      `${problem.slug}.md`
    );

    const markdown =
      generateMarkdown(problem);

    fs.writeFileSync(
      filePath,
      markdown,
      "utf8"
    );

    generated++;

    console.log(
      `Generated: ${problem.slug}.md`
    );
  }

  console.log(
    "\n=============================================="
  );

  console.log(
    "GENERATION COMPLETED"
  );

  console.log(
    "=============================================="
  );

  console.log(
    `Generated: ${generated}`
  );

  console.log(
    `Skipped: ${skipped}`
  );

  console.log(
    `Output: ${outputDir}`
  );

  console.log(
    "==============================================\n"
  );
}


// ============================================================
// RUN
// ============================================================

generateFiles();