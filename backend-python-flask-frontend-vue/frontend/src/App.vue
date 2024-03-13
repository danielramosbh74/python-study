<!-- <template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->



<!-- Source: https://charisol.io/how-to-build-a-full-stack-web-application-with-python-and-vue-js/ -->


<template>

  <div>

    <h1> Charisol’s To-Do List</h1>

    <div v-for="(task, index) in tasks" :key="index">

      {{ task }}

      <button @click="removeTask(index)">Remove</button>

    </div>

    <input v-model="newTask" @keydown.enter="addTask" placeholder="Add a new task" />

    <button @click="addTask">Add</button>

  </div>

</template>

 

<script>

export default {

  data() {

    return {

      tasks: [],

      newTask: "",

    };

  },

  mounted() {

    this.fetchTasks();

  },

  methods: {

    fetchTasks() {

      fetch("/api/tasks")

        .then((response) => response.json())

        .then((data) => {

          this.tasks = data;

        });

    },

    addTask() {

      if (this.newTask.trim() !== "") {

        fetch("/api/tasks", {

          method: "POST",

          headers: {

            "Content-Type": "application/json",

          },

          body: JSON.stringify({ task: this.newTask }),

        })

          .then(() => {

            this.newTask = "";

            this.fetchTasks();

          });

      }

    },

    removeTask(index) {

      fetch(`/api/tasks/${index}`, {

        method: "DELETE",

      })

        .then(() => {

          this.fetchTasks();

        });

    },

  },

};

</script>

