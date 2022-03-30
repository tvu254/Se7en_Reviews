<template>
    <div>
        <div class = "logoutButton">
            <button v-on:click="logout">
                Logout
            </button>
        </div>
    </div>
</template>

<script>
import { reactive,  computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute, useRouter } from 'vue-router';

export default {
  name: 'Edit',
  setup() {
      const store = useStore();
      const route = useRoute();
      const router = useRouter();
      const user = computed(() => store.state.User.user);

    // 4.20: clicking on the review expands it. For when we have more info there
    // ?: prevent submitting when over character limit
    // 5.6: Add stats to user like average rating, past likes, total likes, etc. I think we should remove followers and just have average review rating and number of ratings. That way famous people's opinions wouldnt be more important
    // 9: Add security to passwords
    // ?: get invalid state to work for login/register - currently works every time except the first time lol
    // ?: Add redirects to homepage/browse when necessary (right domain, wrong extension | or review that doesnt exist, etc)
    // ?: Be able to edit specific values of your review - could be added as a separate page, linked to by both profile and post
    // ?: Add click outside functionality for dropdown boxes
    // fix the "nothing yet :)" from showing bc it takes a sec to load --> did not say nothing yet when testing just now
    // ?: Order the reviews in reverse-id order so the newest is at front
    // ?: Gradually load reviews on browse instead of all at once
    // else: Deploy app as website, get user testing


    // BY PRESENTATION DAY
    // delete/edit review
    //    ^--> this requires a drop-down box when clicking review. Asks for edit or delete. Edit will have to be it's own component. Data sent to flask will replace every value in current review, then entered. Delete asks if you are sure  
 

      const state = reactive({
        followers: 0,
        userTestVal: '',
        notLoggedIn: false
      })

      const logout = async () => {
        await store.dispatch('User/setUser', null);
        await router.push('/');
      }

    return {
        state,
        toggleFavorite,
        userId,
        logout,
        user
    }
  },
}
</script>

<style lang="scss" scoped>


</style>
