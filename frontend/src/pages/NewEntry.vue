<!-- created by Allison with help from Gemini and ChatGPT -->

<script setup lang="ts">
import { ref } from 'vue';

// 1. Calculate Today's date in YYYY-MM-DD format
// We split by 'T' to get just the date part (e.g. "2025-12-09")
const maxDate = new Date().toISOString().split('T')[0] ?? '';
const date = ref('');
const workOn = ref('');
const learned = ref('');
const stuckOn = ref('');

// Replace with your actual API Gateway URL
const API_URL = 'https://eljino7joe.execute-api.us-east-1.amazonaws.com/entries'; 

const saveEntry = async () => {
  // 2. Logic Check: Prevent submission if date is in the future
  if (date.value > maxDate) {
    alert("You cannot add an entry for a future date.");
    return;
  }

  const payload = {
    userId: "DemoUser",
    date: date.value,
    workedOn: workOn.value,
    learned: learned.value,
    stuckOn: stuckOn.value
  };

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (response.ok) {
      alert('Entry Saved!');
      // Clear form
      date.value = '';
      workOn.value = '';
      learned.value = '';
      stuckOn.value = '';
    } else {
      alert('Error saving entry');
    }
  } catch (error) {
    console.error(error);
    alert('Network error');
  }
};
</script>

<template>
  <h1>New Entry</h1>

  <form @submit.prevent="saveEntry">
    <label for="date">Date</label>
    <input 
      v-model="date" 
      type="date" 
      id="date" 
      :max="maxDate" 
      required 
    />

    <label for="workOn">What did you work on?</label>
    <input v-model="workOn" type="text" id="workOn" placeholder="e.g. Built a to-do app" required />

    <label for="learned">What did you learn?</label>
    <input v-model="learned" type="text" id="learned" placeholder="e.g. Learned about Vue.js" required />

    <label for="stuckOn">What were you stuck on?</label>
    <input v-model="stuckOn" type="text" id="stuckOn" placeholder="e.g. Debugging a component" required />

    <button type="submit">Save Entry</button>
  </form>
</template>

<style scoped>
form {
    background: #ffffff;
    padding: 1.5rem;
    margin-top: 1rem;
    border-radius: 14px;
    border: 1px solid #d9e6db;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

label {
    font-size: 0.95rem;
    font-weight: 600;
    color: #31493c;
    margin-top: 0.5rem;
}

input[type="text"],
input[type="date"] {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1.5px solid #c8d7ce;
    border-radius: 10px;
    background: #ffffff;
    font-size: 1rem;
    transition: border 0.2s ease, box-shadow 0.2s ease;
    box-sizing: border-box;
}

input[type="text"]:focus,
input[type="date"]:focus {
    border-color: #3e8e57;
    box-shadow: 0 0 4px rgba(62, 142, 87, 0.25);
    outline: none;
}

button[type="submit"] {
    align-self: flex-start;
    background: #3e8e57;
    color: #ffffff;
    padding: 0.45rem 1.2rem;
    font-size: 0.95rem;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.2s ease, transform 0.1s ease;
}

button[type="submit"]:hover {
    background: #2f6e44;
}

button[type="submit"]:active {
    transform: scale(0.97);
}
</style>
