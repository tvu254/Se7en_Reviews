<template>
<div class = "reviewItem" @click="favoriteReview(review.id)">
    <div class = "userProfileReview">
        <div class = "userReviewItem">
            {{ username }}
        </div>
        <div class = "reviewContext"> 
            Type - {{ review.type }}
            <div>
                Genre - {{ review.genre }} 
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
}
</style>