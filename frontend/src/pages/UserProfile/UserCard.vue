<template>
  <md-card class="md-card-profile">
    <div class="md-card-avatar">
      <img class="img" :src="cardUserImage" />
    </div>

    <md-card-content>
      <h6 class="category text-gray">Bot Newbie</h6>
      <h4 class="card-title">{{userName}}</h4>
      <!-- <p class="card-description">
        Don't be scared of the truth because we need to restart the human
        foundation in truth And I love you like Kanye loves Kanye I love Rick
        Owens’ bed design but the back is...
      </p> -->
      <md-button class="md-round md-success">Follow</md-button>
    </md-card-content>
  </md-card>
</template>
<script>
export default {
  name: "user-card",
  props: {
    cardUserImage: {
      type: String,
      default: require("@/assets/img/bot-logo.png")
    }
  },
  data: function(){
    return {
        userName: ''          
    };
  },
  created: async function(){
      const uResponse= await fetch("https://3.121.42.191/profile/:userName")
  }
};
</script>
<style></style>
