<template>
<div class = "reviewItem" @click="showOptions(review.id)">
    <div class = "userProfileReview">
        <div class = "userReviewItem">
            {{ username }}
        </div>
        <div class = "reviewContext"> 
            Genre - {{ review.genre }} 

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
                {{ shortReview }} ...<strong class = "readMore"> Read more</strong>
            </div>
            <div v-if="fullReview == '' && !optionsToggle">
                {{ review.content }}
            </div>
            <div v-if="optionsToggle">
                {{ review.content }}
            </div>
        </div>
        
    </div>
</div>
</template>

<script>
import { ref, computed } from "vue";


export default {
    name: "ReviewItem",
    setup(props, ctx) {

        // make sure accesssing outside of substring doesn't break it. Doesn't seem to right now.
        // Adds functionality for expanding reviews
        const optionsToggle = ref(false);
        const reviewLength = computed(() => props.review.content.length);
        const shortReview = props.review.content.substring(0, 110);
        const fullReview = props.review.content.substring(110, reviewLength.value)


        function showOptions(id) {
            ctx.emit('favorite', id)
            optionsToggle.value = !optionsToggle.value;
        }

        return {
            showOptions,
            optionsToggle,
            reviewLength,
            shortReview,
            fullReview
        }
    },
    props:  {
        username: {
            type: String,
            required: true
        },
        review: {
            type: Object,
            required: true
        }
    }
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

    .readMore {
        color: rgb(82, 82, 82)
    }
}
</style>