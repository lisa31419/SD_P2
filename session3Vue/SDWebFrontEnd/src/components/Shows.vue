<template>
  <div id="app">
    <body style="background-color:lightgrey;">
    <button class='btn btn-success pull-left' @click="goToCart()"> Cart </button>
      <!--h1> {{ message }} </h1>
      <button class="btn btn-success btn-lg" @click="buyTickets"> Buy ticket </button>
      <button class="btn btn-success btn-lg" @click="returnTickets"> Return Ticket </button>
      <h4> Total tickets bought: {{ tickets_bought }} </h4-->
      <div class="container ">
        <div class="row">
          <div class="col-lg-4 col-md-6 mb-4" v-for="(show) in shows" :key="show.id">
            <div class="card text-center" style="width: 18rem;">
              <img class="card-img-top" src="static/image1.jpeg" alt="Card image cap">
              <h4 class="card-header text-center"><b>{{ show.name }}</b></h4>
              <div class="card-body">
                <div v-for="(artist) in show.artists" :key="artist.id">
                  <h5>{{ artist.name }}</h5>
                </div>
                <h6>{{ show.city }}</h6>
                <h6>{{ show.place }}</h6>
                <h6>{{ show.date }}</h6>
                <h6>{{ show.price }} €</h6>
              </div>
            </div>
            <div class="card text-white bg-dark mb-3 text-center" style="max-width: 18rem;">
              <div class="card-body">
                <h4> Tickets available: {{ tickets_available }} </h4>
                <button class="btn btn-success btn-lg" @click="addEventToCart(show)"> Add show to cart </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body>
  </div>
    <!--h4> Price for Event: {{ price_event }} </h4>
    <h4> Money available: {{ money_available }} </h4>
  </div-->
</template>

<script>
import axios from 'axios'

export default {
  name: 'app',
  data () {
    return {
      message: 'My first component',
      tickets_bought: 0,
      price_event: 10,
      money_available: 200,
      shows: [
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
      ],
      shows_added: []
    }
  },
  methods: {
    goToCart () {
      this.$router.push({name: 'CartPage'})
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
    addEventToCart (show) {
      this.shows_added.push(show)
    },
    getShows () {
      const path = 'http://localhost:5000/shows'
      axios.get(path)
        .then((res) => {
          this.shows = res.data.shows
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.getShows()
  }
}
</script>
