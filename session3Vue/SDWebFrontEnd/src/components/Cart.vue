<template>
  <div id="cart">
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Book</button>
        <br><br>
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
                <button type="button" class="btn btn-warning btn-sm">Update
                  <b-icon icon="file-plus-fill" variant="success"></b-icon>
                </button>
                <button type="button" class="btn btn-danger btn-sm">Delete
                  <b-icon icon="file-minus-fill" variant="success"></b-icon>
                </button>
              </div>
            </td>
            <td>foobar</td>
            <td>9</td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
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
