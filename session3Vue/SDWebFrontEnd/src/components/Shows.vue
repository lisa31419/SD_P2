<template>
  <div id="app">
    <h1> {{ message }} </h1>
    <button class="btn btn-success btn-lg" @click="buyTickets"> Buy ticket </button>
    <button class="btn btn-success btn-lg" @click="returnTickets"> Return Ticket </button>
    <h4> Total tickets bought: {{ tickets_bought }} </h4>
    <h4> Price for Event: {{ price_event }} </h4>
    <h4> Money available: {{ money_available }} </h4>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      message: 'My first component',
      tickets_bought: 0,
      price_event: 10,
      money_available: 200
    }
  },
  methods: {
    buyTickets () {
      if (this.money_available !== 0) {
        this.tickets_bought += 1
        this.money_available -= this.price_event
      }
    },
    returnTickets () {
      if (this.tickets_bought !== 0) {
        this.tickets_bought -= 1
        this.money_available += this.price_event
      }
    }
  }
}
</script>
