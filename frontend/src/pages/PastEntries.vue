<script setup lang="ts"></script>

<template>
  <h1>Past Entries</h1>

  <div class="entries-list">
    <div class="entry-card">
      <div class="entry-date">2025-11-08</div>
      <p><strong>Worked on:</strong> Built a login page for a new app I'm working on</p>
      <p><strong>Learned:</strong> How to use DynamoDB keys</p>
      <p><strong>Stuck on:</strong> Figuring out how to fetch data from API Gateway</p>
    </div>

  </div>
  
</template>

<style scoped>
/* I got help from ChatGPT on styling -Allison */
/* Page title */
h1 {
    font-size: 1.6rem;
    color: #1d3b29;
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 1.25rem;
}

/* Container to hold all entry cards */
.entries-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

/* Individual entry card */
.entry-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    border: 1px solid #d6e6d8;

    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);

    display: flex;
    flex-direction: column;
    gap: 0.5rem;

    transition: transform 0.12s ease, box-shadow 0.12s ease;
}

/* Slight lift on hover */
.entry-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
}

/* Date badge */
.entry-date {
    background: #e3efe7;
    color: #2f6e44;

    display: inline-block;
    padding: 0.25rem 0.6rem;

    font-size: 0.85rem;
    font-weight: 600;

    border-radius: 6px;
    margin-bottom: 0.5rem;
}

/* Text styling */
.entry-card p {
    margin: 0;
    line-height: 1.4;
    color: #3c4a41;
    font-size: 0.95rem;
}

.entry-card strong {
    color: #1d3b29;
}
</style>
