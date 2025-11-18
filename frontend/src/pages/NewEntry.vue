<script setup lang="ts"></script>

<template>
  <h1>New Entry</h1>

    <form>
      <label for="date">Date</label>
      <input type="date" id="date" placeholder="mm/dd/yyyy" />

      <label for="workOn">What did you work on?</label>
      <input type="text" id="workOn" placeholder="e.g. Built a to-do app" />

      <label for="learned">What did you learn?</label>
      <input type="text" id="learned" placeholder="e.g. Learned about Vue.js" />

      <label for="stuckOn">What were you stuck on?</label>
      <input type="text" id="stuckOn" placeholder="e.g. Debugging a component" />

      <button type="submit">Save Entry</button>
    </form>

</template>

<style scoped>
/* I got help from ChatGPT on styling -Allison */
/* Form Container */
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

/* Labels */
label {
    font-size: 0.95rem;
    font-weight: 600;
    color: #31493c;
    margin-top: 0.5rem;
}

/* Inputs */
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

/* Button (compact + modern) */
button[type="submit"] {
    align-self: flex-start; /* prevents full-width stretch */

    background: #3e8e57;
    color: #ffffff;

    padding: 0.45rem 1.2rem; /* smaller button */
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
