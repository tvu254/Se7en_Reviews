<template>
  <div class="home">
    <h1><strong>Welcome to uReviews!</strong></h1>
    <h2> Working on connecting app.py, (dynamodb) to load the user reviews instead of the users.js file  </h2>
    <div class="userList">
      <router-link v-for="user in users" :to="{ name: 'UserProfile', params: {userId: user.id} }" :key="user.id">
        {{ user.username }}
      </router-link>
    </div>
  </div>
</template>

<script>
import { users } from "../assets/users";

export default {
  name: 'Home',
  setup() {
    return {
      users
    }
  }
}
</script>

<style lang="scss" scoped>
.home {
  padding: 50px 5%;

  .userList {
    display: flex;
    flex-direction: column;
  }
}
</style>
