<template>
  <div class="home">
    <h1><strong>Welcome to uReview!</strong></h1>
    <h2> This is the uReview alpha version. Feel free to explore features such as login, browse, and post! We are going to implement future features such as
         comments, ratings, search, and more. Thank you for visiting! We will soon be adding artists, songnames, and albums to reviews, as well as the 
         ability to edit and delete reviews
    </h2>
    <br>
    <div class="userList">
      <strong>Featured Reviews</strong>
      <br>
      <br>

      <router-link v-for="user in users" :to="{ name: 'UserProfile', params: {userId: user.id} }" :key="user.id">
        {{ user.username }}
      </router-link>
  </div>
          <div v-show="state.loaded">
        <div v-for="user in userList" :key = "user.reviews">
            <strong>{{ user.UserID }}'s </strong> reviews:
                <ReviewItem     
                    v-for="review in user.reviews" 
                    :key = "review.id" 
                    :username = "UserID" 
                    :review = "review" 
                    @favorite = "toggleFavorite"
                />
                <br>
                <br>
        </div>
    </div>
   </div>

</template>

<script>
import { onMounted, reactive } from "vue";
import ReviewItem from "../components/ReviewItem.vue"


export default {
    name: "Browse",
    components: { ReviewItem },
    setup() {
        onMounted(() => {
            getUsers();
        })
        let userList = []
        const state = reactive({
                loaded: false
        })

        function getUsers() {
            fetch('http://localhost:5000/browse', {
                method: "GET",
            })
            .then(resp => resp.json())
            .then(data => {
                for(let i = 0; i < 5; i++) {
                    userList.unshift(data.Items[i])
                }
                state.loaded = true
                console.log(userList[1].reviews[1])
            })
            .catch(function (error) {
                console.warn('Something went horribly wrong.', error);
            });
        }

        return {
            getUsers,
            state,
            userList
        }
      },
    };
</script>

<style lang="scss" scoped>
.home {
  padding: 50px 5%;
  text-align: center;

  .userList {
    display: flex;
    flex-direction: column;
    font-size: 22px;
  }
}
</style>
