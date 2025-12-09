<!-- created by Allison with help from Gemini and ChatGPT -->

<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface Entry {
  'Date': string;
  'Worked On': string;
  'Learned': string;
  'Stuck On': string;
  isEditing?: boolean;
  editWorkedOn?: string;
  editLearned?: string;
  editStuckOn?: string;
}

const entries = ref<Entry[]>([]);
const isLoading = ref(true);

const API_URL = 'https://eljino7joe.execute-api.us-east-1.amazonaws.com/entries'; 

// Fetch Entries
onMounted(async () => {
  await fetchEntries();
});

const fetchEntries = async () => {
  try {
    const response = await fetch(`${API_URL}?userId=DemoUser`);
    const data = await response.json();
    entries.value = data.sort((a: Entry, b: Entry) => 
      new Date(b.Date).getTime() - new Date(a.Date).getTime()
    );
  } catch (error) {
    console.error("Failed to fetch", error);
  } finally {
    isLoading.value = false;
  }
};

// Start Edit
const startEdit = (entry: Entry) => {
  entry.isEditing = true;
  entry.editWorkedOn = entry['Worked On'];
  entry.editLearned = entry['Learned'];
  entry.editStuckOn = entry['Stuck On'];
};

// Cancel Edit
const cancelEdit = (entry: Entry) => {
  entry.isEditing = false;
};

// Save Edit (PUT)
const saveEdit = async (entry: Entry) => {
  const payload = {
    userId: "DemoUser",
    date: entry.Date,
    workedOn: entry.editWorkedOn,
    learned: entry.editLearned,
    stuckOn: entry.editStuckOn
  };

  try {
    const response = await fetch(API_URL, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (response.ok) {
      entry['Worked On'] = entry.editWorkedOn!;
      entry['Learned'] = entry.editLearned!;
      entry['Stuck On'] = entry.editStuckOn!;
      entry.isEditing = false;
      alert("Entry updated!");
    } else {
      alert("Failed to update.");
    }
  } catch (e) {
    alert("Network error.");
  }
};

// DELETE Entry
const deleteEntry = async (date: string) => {
  // 1. Confirm with the user first
  if (!confirm("Are you sure you want to delete this entry? This cannot be undone.")) {
    return;
  }

  try {
    // 2. Send DELETE request with Query Params
    const response = await fetch(`${API_URL}?userId=DemoUser&date=${date}`, {
      method: 'DELETE',
    });

    if (response.ok) {
      // 3. Remove the item from the local list immediately
      entries.value = entries.value.filter(entry => entry.Date !== date);
      alert("Entry deleted.");
    } else {
      alert("Failed to delete entry.");
    }
  } catch (e) {
    console.error(e);
    alert("Network error during delete.");
  }
};
</script>

<template>
  <h1>Past Entries</h1>
  
  <div v-if="isLoading" class="loading">Loading entries...</div>

  <div class="entries-list">
    <div v-for="entry in entries" :key="entry.Date" class="entry-card">
      <div class="card-header">
        <span class="entry-date">{{ entry.Date }}</span>
        
        <div class="actions" v-if="!entry.isEditing">
          <button @click="startEdit(entry)" class="edit-btn">Edit</button>
          <button @click="deleteEntry(entry.Date)" class="delete-btn">Delete</button>
        </div>
      </div>

      <div v-if="!entry.isEditing">
        <p><strong>Worked on:</strong> {{ entry['Worked On'] }}</p>
        <p><strong>Learned:</strong> {{ entry['Learned'] }}</p>
        <p><strong>Stuck on:</strong> {{ entry['Stuck On'] }}</p>
      </div>

      <div v-else class="edit-form">
        <label>Worked on:</label>
        <input v-model="entry.editWorkedOn" type="text" />
        
        <label>Learned:</label>
        <input v-model="entry.editLearned" type="text" />
        
        <label>Stuck on:</label>
        <input v-model="entry.editStuckOn" type="text" />

        <div class="button-group">
          <button @click="saveEdit(entry)" class="save-btn">Save</button>
          <button @click="cancelEdit(entry)" class="cancel-btn">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 { font-size: 1.6rem; color: #1d3b29; text-align: center; margin-top: 1rem; margin-bottom: 1.25rem; }
.entries-list { display: flex; flex-direction: column; gap: 1rem; }
.entry-card { background: #ffffff; border-radius: 12px; padding: 1rem 1.25rem; border: 1px solid #d6e6d8; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05); }
.card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; }
.entry-date { background: #e3efe7; color: #2f6e44; padding: 0.25rem 0.6rem; font-size: 0.85rem; font-weight: 600; border-radius: 6px; }
p { margin: 0.25rem 0; line-height: 1.4; color: #3c4a41; }
strong { color: #1d3b29; }

/* Action Buttons */
.actions { display: flex; gap: 1rem; }
.edit-btn { background: none; border: none; color: #666; font-size: 0.85rem; cursor: pointer; text-decoration: underline; }
.delete-btn { background: none; border: none; color: #d9534f; font-size: 0.85rem; cursor: pointer; text-decoration: underline; }
.delete-btn:hover { color: #c9302c; }

/* Edit Mode Styles */
.edit-form { display: flex; flex-direction: column; gap: 0.5rem; }
.edit-form input { padding: 0.5rem; border: 1px solid #ccc; border-radius: 4px; }
.button-group { display: flex; gap: 0.5rem; margin-top: 0.5rem; }
.save-btn { background: #3e8e57; color: white; border: none; padding: 0.4rem 0.8rem; border-radius: 4px; cursor: pointer; }
.cancel-btn { background: #ccc; color: black; border: none; padding: 0.4rem 0.8rem; border-radius: 4px; cursor: pointer; }
</style>
