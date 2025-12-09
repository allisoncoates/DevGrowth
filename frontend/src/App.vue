<!-- created by Allison with help from ChatGPT and Gemini -->

<script setup lang="ts">
import { ref, onMounted } from 'vue';

// State for the streak
const streak = ref(0);
const loading = ref(true);

const API_URL = 'https://eljino7joe.execute-api.us-east-1.amazonaws.com/entries'; 

onMounted(async () => {
  try {
    // 1. Fetch all entries for the user
    const response = await fetch(`${API_URL}?userId=DemoUser`);
    const data = await response.json();
    
    // 2. Calculate Streak
    calculateStreak(data);
  } catch (error) {
    console.error("Could not fetch streak", error);
  } finally {
    loading.value = false;
  }
});

const calculateStreak = (entries: any[]) => {
    if (!entries || entries.length === 0) {
        streak.value = 0;
        return;
    }

    // A. Get all unique dates from entries into a Set to remove duplicates
    // expecting dates in "YYYY-MM-DD" format
    const entryDates = new Set(entries.map(e => e.Date));

    // B. Get "Today" and "Yesterday" in YYYY-MM-DD format (Local Time)
    const today = new Date();
    const yesterday = new Date();
    yesterday.setDate(today.getDate() - 1);

    const fmt = (d: Date) => d.toLocaleDateString('en-CA'); // en-CA gives YYYY-MM-DD
    const todayStr = fmt(today);
    const yesterdayStr = fmt(yesterday);

    // C. Check if the streak is active
    // The streak is alive if we have an entry for Today OR Yesterday.
    // If the last entry was 2 days ago, the streak is broken (0).
    if (!entryDates.has(todayStr) && !entryDates.has(yesterdayStr)) {
        streak.value = 0;
        return;
    }

    // D. Count backwards
    let currentCount = 0;
    let checkDate = new Date(); // Start checking from Today

    // If we haven't done today yet, that's fine, start counting from yesterday
    if (!entryDates.has(todayStr)) {
        checkDate.setDate(checkDate.getDate() - 1);
    }

    // Loop backwards
    while (true) {
        const checkStr = fmt(checkDate);
        if (entryDates.has(checkStr)) {
            currentCount++;
            checkDate.setDate(checkDate.getDate() - 1); // Move to previous day
        } else {
            break; // Break the chain
        }
    }

    streak.value = currentCount;
};
</script>

<template>
  <header>
      <div class="title-container">
          <h1>DevGrowth</h1>
          <div class="streak-badge" title="Current Streak">
              {{ streak }} Day Streak
          </div>
      </div>
      <p>Track your daily development progress</p>
  </header>
  <nav>
      <router-link to="/">New Entry</router-link>
      <router-link to="/pastentries">Past Entries</router-link>
  </nav>
  <main>
      <router-view></router-view>
  </main>
</template>

<style scoped>
/* I got help from ChatGPT on styling -Allison */
header, nav, main {
    padding: 1rem;
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
    font-family: "Inter", sans-serif;
}

header {
    text-align: center;
    margin-top: 1.5rem;
}

.title-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.25rem;
}

header h1 {
    font-size: 2rem;
    color: #1d3b29;
    font-weight: 700;
    margin: 0;
}

/* Streak Badge Styling */
.streak-badge {
    background: #fff8e1;
    color: #d97706;
    border: 1px solid #fcd34d;
    padding: 0.3rem 0.6rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.9rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    gap: 0.25rem;
}

header p {
    color: #4f5d57;
    font-size: 0.95rem;
    margin: 0;
}

nav {
    display: flex;
    justify-content: center;
    gap: 1rem;
    background: #f2f6f3;
    border-radius: 14px;
    padding: 0.5rem 0.75rem;
    margin-top: 1.5rem;
    border: 1px solid #d6e2d8;
}

nav a {
    flex: 1;
    text-align: center;
    padding: 0.5rem 0.75rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    color: #355a3a;
    transition: background 0.2s ease, color 0.2s ease;
}

nav a:hover {
    background: #e3efe5;
}

nav a.router-link-active {
    background: #3e8e57;
    color: white;
    font-weight: 600;
}

main {
    margin-top: 1rem;
    padding-bottom: 3rem;
}
</style>