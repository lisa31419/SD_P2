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
          <tr>
            <td>foo</td>
            <td>bar
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-danger btn-lg mr-1"> - </button>
                <button type="button" class="btn btn-success btn-lg "> + </button>
              </div>
            </td>
            <td>foobar</td>
            <td>9</td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-danger btn-md">Delete Ticket</button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
    <div class="card-footer" style="text-align: center;">
      <button class="btn btn-danger btn-lg down-left"> Back </button>
      <button class="btn btn-success btn-lg down-right"> Finalize Purchase </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cart.vue'
}
</script>

<style scoped>

</style>
