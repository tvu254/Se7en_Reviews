<template>
  <div class="homeAnnouncement">
    <h1><strong>Welcome to uReview!</strong></h1>
    <h2> This  the uReview alpha version. Feel free to explore the features and leave a review of your favorite artist, album or song :) &nbsp;
         Comments, ratings, search, review editing, as well as stylistic updates are coming soon. Thank you for visiting!
    </h2>
    <br>
  </div>

    <div class="homeReleases">
     <h1>Upcoming Releases</h1>
  <img src="../assets/zeit.jpg" alt="Zeit by Ramnstein" title= "Zeit by Ramnstein" style="width:12.5%; margin: 0px 5px">
  <img src="../assets/voltage.jpg" alt="Voltage by Itzy" title= "Voltage by Itzy" style="width:12.5%; margin: 0px 5px">
  <img src="../assets/kdm.jpg" alt="Krewe De L'amour by Cane Hill" title= "Krewe De L'amour by Cane Hill" style="width:12.5%; margin: 0px 5px">
  <img src="../assets/ineverdie.jpg" alt="I NEVER DIE by (G)I-dle" title= "I NEVER DIE by (G)I-dle" style="width:12.5%; margin: 0px 5px">
  <img src="../assets/htcs.jpg" alt="Head in the Clouds Forever by 88rising" title= "Head in the Clouds Forever by 88rising" style="width:12.5%; margin: 0px 5px">
</div>

    <div class="userList">
      <div class = "featured">
        <strong>Featured Reviews</strong>
      </div>
      <br>
      <br>

<!--  For reference later
      <div v-show="state.loaded">
        <router-link v-for="user in userList" :to="{ name: 'UserProfile', params: {userId: user.UserID} }" :key="user.UserID">
          {{ user.username }}
        </router-link>
      </div>
-->

      <div v-show="state.loaded">
        <div v-for="user in userList" :key = "user.reviews">
          <div v-if="user.reviews.length != 0">
            <router-link :to="`/user/${user.UserID}`">
              <strong>{{ user.UserID }}'s </strong>
            </router-link> 
                reviews:
                <ReviewItem     
                    v-for="review in user.reviews" 
                    :key = "review.id" 
                    :username = "UserID" 
                    :loggedIn = "false"
                    :review = "review"
                    @favorite = "toggleFavorite"
                />
                <br>
                <br>
            </div>
        </div>
    </div>
   </div>

</template>

<script>
/*
      <div v-show="state.loaded">
        <router-link v-for="user in userList" :to="{ name: 'UserProfile', params: {userId: user.userID} }" :key="user.UserID">
          {{ user.username }}
        </router-link>
      </div>
      */
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
            fetch('http://3.133.58.37:5000/browse', {
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

.homeAnnouncement {
  position: relative;
  height: 150px;
  width: 900px;
  margin: auto;
  //padding: 50px 50px;
  background-size: cover;
  text-align: center;

  .userList {
    display: flex;
    flex-direction: column;
    font-size: 22px;
  }

  .featured {
    padding-top: 30px;
    text-decoration: underline;
    font-size: 28px;
  }
}

.homeReleases {
  position: center;
  margin: auto;
  padding: 100px 50px;
  text-align: center;
}
</style>
