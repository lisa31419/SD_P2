<template>
  <div id="cart">
  <div class="container center-h center-v">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="card-header text-center"><b>Cart</b></h1>
        <hr><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Event Name</th>
            <th scope="col">Quantity</th>
            <th scope="col">Total Price</th>
            <th scope="col">Total Tickets</th>
            <th scope="col"></th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <div v-for="(show) in shows_cart" :key="show.id">
          <tr>
            <td>{{show.name}}</td>
            <td>9
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-danger btn-lg mr-1" @click="returnTickets()"> - </button>
                <button type="button" class="btn btn-success btn-lg " @click="buyTickets()"> + </button>
              </div>
            </td>
            <td>{{show.price}}</td>
            <td>9</td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-danger btn-md">Delete Ticket</button>
              </div>
            </td>
          </tr>
          </div>
          </tbody>
        </table>
      </div>
    </div>
  </div>
    <div class="card-footer" style="text-align: center;">
      <button class="btn btn-danger btn-lg down-left" @click="goToShows()"> Back </button>
      <button class="btn btn-success btn-lg down-right"> Finalize Purchase </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Cart.vue',
  data () {
    return {
      tickets_bought: 0,
      price_event: 10,
      money_available: 200,
      shows_cart: [
        {
          name: 'Festival Cruilla 2020',
          artists: [
            {
              'name': 'Bad Gyal'
            },
            {
              'name': 'Txarango'
            },
            {
              'name': 'Estopa'
            }
          ],
          city: 'Barcelona',
          place: 'Parc del Forum',
          date: '2020-07-03',
          price: 100,
          tickets_available: 100
        },
        {
          name: 'Canet Rock 2020',
          artists: [
            {
              'name': 'Txarango'
            },
            {
              'name': 'Dvicio'
            },
            {
              'name': 'Lola Indigo'
            }
          ],
          city: 'Barcelona',
          place: 'Parc del Forum',
          date: '2020-07-05',
          price: 24,
          tickets_available: 100
        },
        {
          name: 'Iron Maiden Tour',
          artists: [
            {
              'name': 'Iron Maiden'
            }
          ],
          city: 'Barcelona',
          place: 'Sant Jordi',
          date: '2020-08-22',
          price: 70,
          tickets_available: 100
        }
      ]
    }
  },
  methods: {
    goToShows () {
      this.$router.push('/')
    },
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
    },
    getCartShows () {
      const path = 'http://localhost:8080/'
      axios.get(path)
        .then((components) => {
          this.shows_cart = components.data.shows_added
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

<style scoped>

</style>
