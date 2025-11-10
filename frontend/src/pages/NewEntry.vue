<script setup lang="ts"></script>

<template>
  <h1>New Entry</h1>

    <form>
      <label for="date">Date</label>
      <input type="date" id="date" placeholder="mm/dd/yyyy" />

      <label for="workOn">What did you work on?</label>
      <input type="text" id="workOn" placeholder="e.g., Built a to-do app" />

      <label for="learned">What did you learn?</label>
      <input type="text" id="learned" placeholder="e.g., Learned about Vue.js" />

      <label for="stuckOn">What were you stuck on?</label>
      <input type="text" id="stuckOn" placeholder="e.g., Debugging a component" />

      <button type="submit">Save Entry</button>
    </form>

</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
</style>
