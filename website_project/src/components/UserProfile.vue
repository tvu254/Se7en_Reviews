<template>
    <div class = "userProfile">
        <div class = "userProfilePanel">
            <h1 class = "userProfileUsername">{{ fullName }}  -  @{{ user.username }}</h1>
         <div class = "verifiedBadge" v-if="user.isVerified">
             Verified
         </div>
        <div class = "userProfileFollowerCt">
            <strong> Followers: </strong> {{ followers }}
        </div>
        <form class = "createReview" @submit.prevent = "createNewReview">
            <label for = "newReview"> <strong>New Review</strong> </label>
            <textarea id="newReview" rows = "4" v-model = "newReviewContent"/>

            <div class = "creatReviewType">
                <label for="newReviewType"> <strong>Type: </strong> </label>
                    <select id = "newReviewType" v-model = "selectedReviewType">
                        <option :value = "option.value" v-for = "(option, index) in reviewTypes" :key = "index">
                            {{ option.name }}
                        </option>
                    </select>
            </div>
            <button>
                Post Review
            </button>
        </form>
        </div>
    </div>
      <div class = "followButton">
        <button v-on:click="followUser">
            Follow
        </button>
    </div>
    <div class = "userReviewsWrapper">
        @{{user.username}}'s Reviews:
        <ReviewItem 
            v-for="review in user.reviews" 
            :key = "review.id" 
            :username = "user.username" 
            :review = "review" 
            @favorite = "toggleFavorite"
        />
    </div>
</template>

<script>
import ReviewItem from "./ReviewItem.vue"

export default {
  name: 'UserProfile',
  components: { ReviewItem },
  data() {
    return {
        newReviewContent: '',
        selectedReviewType: 'choose',
        reviewTypes: [
            { value: 'choose', name: 'Choose' },
            { value: 'music', name: 'Music' },
            { value: 'game', name: 'Game' },
            { value: 'movie', name: 'Movie' },
        ],
      followers: 0,
      user: {
        id: 1,
        username: 'Jakobeus',
        firstName: 'Jacob',
        lastName: 'Benz',
        email: 'thejacobbenz@gmail.com',
        isVerified: true,
        reviews: [
            { id: 1, type: 'Music', genre: 'Alternative/indie',  content: 'Rainbow kitten Surprise is a great band.'},
            { id: 2, type: 'Music', genre: 'Rock', content: "The Dark Side of the Moon is a fantastic album."}
        ]
      }
    }
  },
  watch: {
    followers(newFollowerCount, oldFollowerCount) {
      if (oldFollowerCount < newFollowerCount) {
        console.log(`${this.user.username} has gained a follower`)
      }
    }
  },
  computed: {
    fullName() {
      return `${this.user.firstName} ${this.user.lastName}`;
    }
  },
  methods: {
    followUser() {
      this.followers++
    },
    toggleFavorite(id) {
        console.log(`Favorited Review = ${id}`)
    },
    createNewReview() {
        if (this.newReviewContent && this.selectedReviewType !== 'choose') {
            this.user.reviews.unshift( {
                id: this.user.reviews.length + 1,
                type: this.selectedReviewType,
                genre: 'Kanye',
                content: this.newReviewContent
            })
            this.newReviewContent = '';
        }
    }
  },
  mounted() {
    this.followUser();
  }
}
</script>

<style lang="scss" scoped>

@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');
 
.userProfile {
    display: grid;
    grid-template-columns: 1fr 3fr;
    grid-gap: 50px;
    padding: 50px 5%;
}

.userProfilePanel {
    display: flex;
    flex-direction: column;
    padding: 20px;
    background-color: 0d1424;
    border-radius: 5px;
    border: 1px solid #DFE3E8;
}

.verifiedBadge {
    background: rgb(153, 20, 170);
    color: white;
    border-radius: 5px;
    margin-right: auto;
    padding: 0 10px;
    font-weight: bold;
    margin-top: 5px;
    margin-bottom: 5px;
}

h1 {
    margin: 0;
    font-size: 28px;
}

.followButton {
    text-align: center;
}

.userReviewsWrapper {
    display: grid;
    grid-gap: 10px;
    text-align: center;
    margin-top: 5px;
    color: #a7a7a7;
}

.createReview {
    padding-top: 20px;
    display: flex;
    flex-direction: column;
 }

 .createReviewType {
    border-radius: 5px;
    flex-direction: column;
    box-sizing: border-box;
    text-align: center;
    border: #f0f0f0 solid 1px;
    margin-top: 10px;
}
</style>
