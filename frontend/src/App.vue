<template>
  <div id="nav">
    <header class="header shop">
    <!-- Header Inner -->
    <div class="header-inner">
      <div class="container">
          <div class="cat-nav-head">
              <div class="row">
                  <div class="col-lg-9 col-12">
                      <div class="menu-area">
                          <!-- Main Menu -->
                          <nav class="navbar navbar-expand-lg">
                              <div class="navbar-collapse">
                                  <div class="nav-inner">
                                      <ul class="nav main-menu menu navbar-nav">
                                              <li><router-link to="/">Home</router-link></li>
                                              <li><router-link to="product">Product</router-link></li>
                                              <li><router-link to="service">Service</router-link></li>
                                              <li><router-link to="shop">Shop<i class="ti-angle-down"></i><span class="new">New</span></router-link>
                                                  <ul class="dropdown">
                                                      <li><router-link to="shop-grid">Shop Grid</router-link></li>
                                                      <li><router-link to="cart">Cart</router-link></li>
                                                      <li><router-link to="checkout">Checkout</router-link></li>
                                                  </ul>
                                              </li>
                                              <li><router-link to="pages">Pages</router-link></li>
                                              <li><router-link to="blog">Blog<i class="ti-angle-down"></i></router-link>
                                                      <ul class="dropdown">
                                                          <li><router-link to="blog-single-sidebar">Blog Single Sidebar</router-link></li>
                                                      </ul>
                                                  </li>
                                                  <li><router-link to="contact">Contact Us</router-link></li>
                                              </ul>
                                      </div>
                                  </div>
                              </nav>
                              <!--/ End Main Menu -->
                          </div>
                      </div>
                  </div>
              </div>
          </div>
        </div>
        <!--/ End Header Inner -->
    </header>
  <router-view/>
  </div>
</template>

<style lang="scss">
.router-link-active {
 color:#fff;
 background:#F7941D;
}
</style>
