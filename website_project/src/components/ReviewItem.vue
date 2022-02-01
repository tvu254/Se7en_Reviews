<template>
<div class = "reviewItem" @click="favoriteReview(review.id)">
    <div class = "userReview">
        <div class = "userReviewItem">
            @{{ username }}
            <div class = "reviewContext"> 
                Type - {{ review.type }}
                <div>Genre - {{ review.genre }} </div>
            </div>
        </div>
        <div class = "reviewItemContent">
            {{ review.content }}
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "ReviewItem",
    props: {
        username: {
            type: String,
            required: true
        },
        review: {
            type: Object,
            required: true
        }
    },
    methods: {
        favoriteReview(id) {
            this.$emit('favorite', id)
        }
    }
};
</script>

<style scoped>
.reviewItem {
    padding: 20px;
    background-color: #0d1424;
    border-radius: 5px;
    border: 1px solid #a7a7a7;
    box-sizing: border-box;
    cursor: pointer;
    transition: all 0.24s ease;
    width: 550px;
    margin: auto;
    margin-top: 5px;
}

.reviewItem:hover {
    transform: scale(1.1, 1.1);
}
.userReviewItem {
     font-weight: bold;
 }

.reviewContext {
    font-weight: normal;
}
</style>