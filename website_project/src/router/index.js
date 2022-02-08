import { createRouter, createWebHistory } from 'vue-router';
import store from '../store';
import { users } from "../assets/users";
import Home from '../views/Home.vue';
import UserProfile from "../views/UserProfile";
import Admin from "../views/Admin";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/user/:userId',    // uses userId as variable in URL
    name: 'UserProfile',
    component: UserProfile
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
    meta: {
      requiresAdmin: true
    }
  }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// router guard
router.beforeEach(async (to, from, next) => {
  const user = store.state.User.user;

  if (!user) {
    // fetch user from db once db connected, this just sets state as first user - will eventually need to be connected to register/login
    await store.dispatch('User/setUser', users[0])   // dispatches action 'setUser' with data users[0] from users.js file
  }

  const isAdmin = true; // should actually reference user
  const requiresAdmin = to.matched.some(record => record.meta.requiresAdmin);

  if (requiresAdmin && !isAdmin) next({ name: 'Home' })   // if needs admin but !admin, go home
  else next();
})

export default router
