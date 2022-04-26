<template>
<div class = "reviewItem" @click="showOptions(review.id)">
    <div class = "userProfileReview">
      <div v-if="!state.edit">
        <div class = "userReviewItem">
            <!--{{ username }}-->
        </div>
        <div class = "reviewContext"> 
            <!--Genre - {{ review.genre }}-->

            <div v-if="review.artist != ''">
                Artist - {{ review.artist }} 
            </div>
            <div v-if="review.album != ''">
                Album - {{ review.album }} 
            </div>
            <div v-if="review.songname != ''">
                Song name - {{ review.songname }} 
            </div>
            <br>

        </div>

        <!-- allows reviews to be expanded -->
        <div class = "reviewItemContent">
            <div v-if="fullReview != '' && !optionsToggle">
                {{ shortReview }} ...<strong class = "readMoreShowLess"> Read more</strong>
            </div>
            <div v-if="fullReview == '' && !optionsToggle">
                {{ review.content }}
            </div>
            <div v-if="optionsToggle">
                {{ review.content }}
            </div>
        </div>
        
        <div v-if="optionsToggle && (!fullReview == '')">
            <br>
            <strong class = "readMoreShowLess"> (Click to show less) </strong>
        </div>

        <!-- edit and delete here // set ONLY if logged in -->
      <div v-if="loggedIn == true">
        <div v-if="optionsToggle">
            <br>
            <button dark class="button" @click="deleteReview(review.id)">
                Delete
            </button>
            &nbsp; &nbsp;      
        <!--<router-link :to="{ name: 'Edit', params: {reviewId: review.id} }" :key="username">-->
            <button dark class="button" @click="EditReview(review.id)">
                Edit
            </button>
        <!--</router-link>-->
        </div>
      </div>
     </div>
     <div v-else>
        <div v-if="state.delete">
            <Delete :username = "username" :review = "review" :edit = "state.edit" @showOptions = "showOptions"/>
        </div>
        <div v-else>
            <Edit :username = "username" :review = "review" :edit = "state.edit" @showOptions = "showOptions"/>
        </div>
     </div>
    </div>
</div>
</template>

<script>
import { ref, computed, reactive } from "vue";
import Edit from "../views/Edit.vue";
import Delete from "../components/Delete.vue"


export default {
    name: "ReviewItem",
    setup(props) {
        // make sure accesssing outside of substring doesn't break it. Doesn't seem to right now.
        // Adds functionality for expanding reviews
        const optionsToggle = ref(false);
        const reviewLength = computed(() => props.review.content.length);
        const shortReview = props.review.content.substring(0, 95);
        const fullReview = props.review.content.substring(95, reviewLength.value);
        const state = reactive({
            edit: false,
            delete: false
        });

        // state v-if edit-on --> on every review. Edit switches this
        function showOptions() {
            optionsToggle.value = !optionsToggle.value;
        }
        function deleteReview(id) {
            // need to call delete after asking if sure
            console.log(`in delete, id = ${id}`);
            state.edit = !state.edit;
            state.delete = !state.delete;
            optionsToggle.value = !optionsToggle.value;
            //ctx.emit("deleteReview", id);
        }
        function EditReview(id) {
            console.log(`in edit, id = ${id}`);
            state.edit = !state.edit;
            console.log(state.edit);
            optionsToggle.value = !optionsToggle.value;
        }
        return {
            showOptions,
            optionsToggle,
            reviewLength,
            shortReview,
            fullReview,
            EditReview,
            deleteReview,
            state
        };
    },
    props: {
        username: {
            type: String,
            required: true
        },
        loggedIn: {
            type: Boolean,
            required: true
        },
        review: {
            type: Object,
            required: true
        }
    },
    components: { Edit, Delete }
};
</script>

<style lang="scss" scoped>
.reviewItem {
    padding: 12px;
    background-color: #ececec;
    border-radius: 5px;
    border: 1px solid #0d1424;
    box-sizing: border-box;
    cursor: pointer;
    transition: all 0.24s ease;
    width: 550px;
    margin: auto;
    margin-top: 5px;
    //font-size: 18px;   --> if I use serif instead of arial

    &:hover {
        transform: scale(1.1, 1.1);
    }

    .userReviewItem {
        font-weight: bold;
    }

    .reviewContext {
        font-weight: normal;
    }

    .readMoreShowLess {
        color: rgb(82, 82, 82);
        padding: 0;
        border: none;
        background: none;
    }
}


</style>


//  background: rgba(0, 97, 161, 0.9);
<!-- HTML !-->
<button class="button-24" role="button">Button 24</button>

/* CSS */
