from bs4 import BeautifulSoup
import re

html_source_code = """



<body class="store-locator-locations consumer" data-new-gr-c-s-check-loaded="14.1115.0" data-gr-ext-installed="">
    <!-- Google Tag Manager (noscript) -->
    <noscript>
        <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WFZZM99"
                height="0" width="0"
                style="display:none;visibility:hidden"></iframe>
    </noscript>
    <!-- End Google Tag Manager (noscript) -->

    <div class="header-container"><nav id="consumer-nav" class="navbar navbar-fixed-top dolla" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed navbar-left" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand dolla-brand icon-DOLLARAMA_LOGO grunt-logo" href="https://www.dollarama.com/">
<!--                <img src="https://www.dollarama.com/en-CA/corp/--><!--/resources/images/logo.png" class="navbar-image img-responsive" alt="Dollarama" width="210"/>-->
            </a>
        </div>

        <div id="navbar" class="collapse navbar-collapse">
            <div class="hidden-md hidden-lg" id="mobile-nav">
                <ul id="menu-main" class="nav navbar-nav"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1639"><a href="https://www.dollarama.com/en-CA/locations/">Find a Store</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-37"><a href="https://www.dollarama.com/en-CA/corp/careers">Careers</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-70"><a target="_blank" rel="noopener" href="https://www.dollarama.com/en-CA/corp/investor-relations">Investor Relations</a></li>
</ul>
                <ul id="mobile-secondary-nav" class="nav navbar-nav">
                    <li><a class="language" href="https://www.dollarama.com/fr-CA/carrieres/localisateur/magasins-pres-de-moi/?jobCode=SA&amp;kilometers=10&amp;lat=50.44876&amp;lng=-104.61731">Français</a></li>                </ul>

            </div>

            <div class="hidden-xs hidden-sm" id="fullsize-nav">
                <div id="secondary-nav-wrapper" class="nav navbar-nav navbar-right">
                    <a id="secondary-nav" class="language" href="https://www.dollarama.com/fr-CA/carrieres/localisateur/magasins-pres-de-moi/?jobCode=SA&amp;kilometers=10&amp;lat=50.44876&amp;lng=-104.61731">Français</a>                </div>

                <ul id="main-nav" class="nav navbar-nav navbar-right"><li class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item menu-item-1639"><a href="https://www.dollarama.com/en-CA/locations/">Find a Store</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-37"><a href="https://www.dollarama.com/en-CA/corp/careers">Careers</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-70"><a target="_blank" rel="noopener" href="https://www.dollarama.com/en-CA/corp/investor-relations">Investor Relations</a></li>
</ul>            </div>
        </div>
    </div>
</nav></div>
    <input type="hidden" id="jsLinkPrefix" value="https://www.dollarama.com/en-CA/locations/">
    <input type="hidden" id="jsResPrefix" value="https://www.dollarama.com/en-CA/locations/">
  
    <script>
        var IsCareersPage = $("html").hasClass("careers");
        $(".header-container").load(jsResPrefix.value + "GetHeaderFooter #consumer-nav", function () {
            //setHeaderTracking();
            var toggleUrl = 'https://www.dollarama.com/fr-CA/carrieres/localisateur/magasins-pres-de-moi/?jobCode=SA&kilometers=10&lat=50.44876&lng=-104.61731';
            if (IsCareersPage) {
                if ("en-US" == "fr-CA")
                    toggleUrl = toggleUrl.replace("/locations/", "/careers/locations/");
                else
                    toggleUrl = toggleUrl.replace("/fr/localisateur/", "/fr/carrieres/localisateur/");
            }

            $(".header-container .language").attr('href', toggleUrl );
            $("li.hover").on("hover", function () {
                var el = $(this).find('span');
                var classList = el.attr('class').split(/\s+/);
                $.each(classList, function (index, item) {
                    if (-1 != item.indexOf('icon-')) {
                        el.toggleClass(item + '_hover');
                    }
                });
            });

            $("span.hover").on("hover", function () {
                var el = $(this);
                var classList = el.attr('class').split(/\s+/);
                $.each(classList, function (index, item) {
                    if (-1 != item.indexOf('icon-')) {
                        el.toggleClass(item + '_hover');
                    }
                });
            });
        });
    </script>


<div class="container padding0">

            <div class="store-locator-hero"><h2 class="h1">Careers<br> Find a store near you to apply!</h2></div>


</div>
<!--form finder-->
<div class="container white-bg">
    <div class="xs-mt-15 xs-m-0 store-locator-form-container">
        <div class="container-header-footer">
            <div class="form">
                <a href="https://www.dollarama.com/en-CA/careers/locations/stores-near-me?current-location=true&amp;kilometers=10&amp;jobCode=SA" class="current-location-btn btn btn-default" target="_self">
                    <img src="https://www.dollarama.com/en-CA/locations/images/marker.png" class="img-responsive" alt="current-location">
                    <span class="current-location-text">Use Current Location</span>
                </a>
                <div class="csee-title">
                    <span class="or">OR</span>
                </div>
                <form id="search" action="https://www.dollarama.com/en-CA/careers/locations/stores-near-me" type="post" data-parsley-validate="">
                    <div class="form-group">
                        <div id="geocoder" class="geocoder"><div class="mapboxgl-ctrl-geocoder mapboxgl-ctrl"><svg class="mapboxgl-ctrl-geocoder--icon mapboxgl-ctrl-geocoder--icon-search" viewBox="0 0 18 18" xml:space="preserve" width="18" height="18"><path d="M7.4 2.5c-2.7 0-4.9 2.2-4.9 4.9s2.2 4.9 4.9 4.9c1 0 1.8-.2 2.5-.8l3.7 3.7c.2.2.4.3.8.3.7 0 1.1-.4 1.1-1.1 0-.3-.1-.5-.3-.8L11.4 10c.4-.8.8-1.6.8-2.5.1-2.8-2.1-5-4.8-5zm0 1.6c1.8 0 3.2 1.4 3.2 3.2s-1.4 3.2-3.2 3.2-3.3-1.3-3.3-3.1 1.4-3.3 3.3-3.3z"></path></svg><input type="text" class="mapboxgl-ctrl-geocoder--input" placeholder="Enter City or Postal Code"><div class="suggestions-wrapper"><ul class="suggestions" style="display: none;"></ul></div><div class="mapboxgl-ctrl-geocoder--pin-right"><button aria-label="Clear" class="mapboxgl-ctrl-geocoder--button"><svg class="mapboxgl-ctrl-geocoder--icon mapboxgl-ctrl-geocoder--icon-close" viewBox="0 0 18 18" xml:space="preserve" width="18" height="18"><path d="M3.8 2.5c-.6 0-1.3.7-1.3 1.3 0 .3.2.7.5.8L7.2 9 3 13.2c-.3.3-.5.7-.5 1 0 .6.7 1.3 1.3 1.3.3 0 .7-.2 1-.5L9 10.8l4.2 4.2c.2.3.7.3 1 .3.6 0 1.3-.7 1.3-1.3 0-.3-.2-.7-.3-1l-4.4-4L15 4.6c.3-.2.5-.5.5-.8 0-.7-.7-1.3-1.3-1.3-.3 0-.7.2-1 .3L9 7.1 4.8 2.8c-.3-.1-.7-.3-1-.3z"></path></svg></button><svg class="mapboxgl-ctrl-geocoder--icon mapboxgl-ctrl-geocoder--icon-loading" viewBox="0 0 18 18" xml:space="preserve" width="18" height="18"><path fill="#333" d="M4.4 4.4l.8.8c2.1-2.1 5.5-2.1 7.6 0l.8-.8c-2.5-2.5-6.7-2.5-9.2 0z"></path><path opacity=".1" d="M12.8 12.9c-2.1 2.1-5.5 2.1-7.6 0-2.1-2.1-2.1-5.5 0-7.7l-.8-.8c-2.5 2.5-2.5 6.7 0 9.2s6.6 2.5 9.2 0 2.5-6.6 0-9.2l-.8.8c2.2 2.1 2.2 5.6 0 7.7z"></path></svg></div></div></div>
                        <div id="mapboxmap" class="mapboxgl-map"><div class="mapboxgl-canary" style="visibility: hidden;"></div><div class="mapboxgl-canvas-container mapboxgl-interactive mapboxgl-touch-drag-pan mapboxgl-touch-zoom-rotate"><canvas class="mapboxgl-canvas" tabindex="0" aria-label="Map" width="660" height="660" style="position: absolute; width: 300px; height: 300px;"></canvas></div><div class="mapboxgl-control-container"><div class="mapboxgl-ctrl-top-left"></div><div class="mapboxgl-ctrl-top-right"></div><div class="mapboxgl-ctrl-bottom-left"><div class="mapboxgl-ctrl" style="display: none;"><a class="mapboxgl-ctrl-logo" target="_blank" rel="noopener" href="https://www.mapbox.com/" aria-label="Mapbox logo"></a></div></div><div class="mapboxgl-ctrl-bottom-right"><div class="mapboxgl-ctrl mapboxgl-ctrl-attrib mapboxgl-compact"><div class="mapboxgl-ctrl-attrib-inner"></div></div></div></div></div>


                        <input id="lat" name="lat" type="hidden">
                        <input id="lng" name="lng" type="hidden">


                    </div>
                    <div class="form-group hide">
                        <label for="form-miles" style="display:none;">Miles</label>
                        <select id="form-miles" name="kilometers">

                                <option value="2">within 2 km</option>
                                <option value="5">within 5 km</option>
                                <option value="10" selected="">within 10 km</option>
                                <option value="15">within 15 km</option>
                                <option value="20">within 20 km</option>
                                <option value="25">within 25 km</option>
                                <option value="30">within 30 km</option>

                        </select>
                    </div>

                    <button type="submit" class="find-btn btn btn-default">Search</button>
                </form>
                <div id="error-box"></div>
            </div>
                <div class="job-filters">
                    <div class="filter-heading"><strong>Filter By Position</strong></div>
                    <div class="filter-body">
                            <div class="form-check form-check-inline">
                                <input form="search" class="form-check-input" id="filter-SM" name="jobCode" type="checkbox" data-code="SM" value="SM" data-name="Store Manager">
                                <label class="form-check-label" for="filter-SM">Store Manager</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input form="search" class="form-check-input" id="filter-TL" name="jobCode" type="checkbox" data-code="TL" value="TL" data-name="Team Leader">
                                <label class="form-check-label" for="filter-TL">Team Leader</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input form="search" class="form-check-input" id="filter-SA" name="jobCode" type="checkbox" data-code="SA" value="SA" data-name="Store Associate">
                                <label class="form-check-label" for="filter-SA">Store Associate</label>
                            </div>
                                <br>
                            <div class="form-check form-check-inline">
                                <input form="search" class="form-check-input" id="filter-ASM" name="jobCode" type="checkbox" data-code="ASM" value="ASM" data-name="Assistant Store Manager">
                                <label class="form-check-label" for="filter-ASM">Assistant Store Manager</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input form="search" class="form-check-input" id="filter-ATL" name="jobCode" type="checkbox" data-code="ATL" value="ATL" data-name="Assistant Team Leader">
                                <label class="form-check-label" for="filter-ATL">Assistant Team Leader</label>
                            </div>
                    </div>
                </div>
        </div>
    </div>
</div>
<style>
    .mapboxgl-canvas {
        left: 0px;
    }

    .marker {
        width: auto;
        height: auto;
        padding-top: 2px;
        cursor: pointer;
        text-align: center;
        font-size: 14px;
        color: #fff;
        margin-top: -23px;
    }

        .marker img {
            width: 50px;
        }

    .suggestions-wrapper {
        text-align: left;
    }

    .marker span {
        padding-top: 8px !important;
        text-align: center;
        display: block;
        height: 57px;
        width: 45px !important;
    }

    .mapboxgl-ctrl-geocoder--icon-search {
        display: none;
    }

    @media screen and (min-width: 992px) {
        .mapboxgl-ctrl-geocoder {
            width: 100%;
            font-size: 15px;
            line-height: 20px;
            max-width: 360px;
            width: 300px;
        }
    }

    @media screen and (max-width: 991px) {
        .mapboxgl-ctrl-geocoder {
            margin-bottom: 20px;
        }

        .mapboxgl-ctrl-geocoder {
            width: 100%;
            max-width: 100%;
        }
    }
</style>




<div class="container white-bg  locations-content">
    

    <div class="found">
        <span>Found </span><span class="store-count"><span class="number">13</span> stores</span>
    </div>

        <div class="search">
            <span class="search-text">Search for stores within:</span>
            <select id="miles">
                <option value="2">2 km</option>
                <option value="5">5 km</option>
                <option value="10" selected="''">10 km</option>
                <option value="15">15 km</option>
                <option value="20">20 km</option>
                <option value="25">25 km</option>
                <option value="30">30 km</option>
            </select>
        </div>
    <div class="stores clearfix">
        <div class="update-search-wrapper hidden-xs"><div class="update-search-button">Search This Area</div></div>
        <div id="list" class="list col-sm-5">
            <div class="no-location-message" style="display: none;">
                    <p class="address-text">No results found</p>
                    <p class="text-50-mile">We couldn't find any open positions for your search. <br> Please try another search.</p>
                    <p class="text-other">We couldn't find any open positions for your search. <br> Please try another search.</p>

            </div>
        <div class="row" data-id="514268a8-17ac-4c1d-8e8e-78c01d6daf1d"><div class="counter">1</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-2102-11th-avenue" data-label="2102 11th Avenue" target="_self"><h3>Dollarama</h3></a><span class="distance">0.5 km</span><span class="storeid">514268a8-17ac-4c1d-8e8e-78c01d6daf1d</span><p class="address">2102 11th Avenue</p><p class="city-postal-code">Regina, SK S4P3Y6</p><a class="directions" href="https://www.google.com/maps/dir//2102 11th Avenue Regina SK" data-label="2102 11th Avenue" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Closed now.</span><br> Opening tomorrow at 12:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 522-9982" class="phone" data-label="306-522-9982" data-tel="+13065229982" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 522-9982</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-2102-11th-avenue" data-label="2102 11th Avenue" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=TL&amp;storeid=522" class="btn btn-default btn-job">Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=522" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=522" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="148c6422-83c2-4b18-970c-9e45778a4b7e"><div class="counter">2</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-1230h-broad-st" data-label="1230H Broad St" target="_self"><h3>Dollarama</h3></a><span class="distance">1.3 km</span><span class="storeid">148c6422-83c2-4b18-970c-9e45778a4b7e</span><p class="address">1230H Broad St</p><p class="city-postal-code">Regina, SK S4R1Y3</p><a class="directions" href="https://www.google.com/maps/dir//1230H Broad St Regina SK" data-label="1230H Broad St" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 569-9722" class="phone" data-label="306-569-9722" data-tel="+13065699722" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 569-9722</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-1230h-broad-st" data-label="1230H Broad St" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=TL&amp;storeid=833" class="btn btn-default btn-job">Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=833" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=833" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="92a90d60-875f-43a1-ac96-ebaf2e63a0e4"><div class="counter">3</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-921-a-albert-st" data-label="921 A. Albert St" target="_self"><h3>Dollarama</h3></a><span class="distance">1.6 km</span><span class="storeid">92a90d60-875f-43a1-ac96-ebaf2e63a0e4</span><p class="address">921 A. Albert St</p><p class="city-postal-code">Regina, SK S4R2P6</p><a class="directions" href="https://www.google.com/maps/dir//921 A. Albert St Regina SK" data-label="921 A. Albert St" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 719-1228" class="phone" data-label="306-719-1228" data-tel="+13067191228" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 719-1228</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-921-a-albert-st" data-label="921 A. Albert St" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=TL&amp;storeid=961" class="btn btn-default btn-job">Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=961" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=961" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="2482435b-dcc2-41b5-8abe-02054f5c92b9"><div class="counter">4</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-3765-sherwood-dr" data-label="3765 Sherwood Dr" target="_self"><h3>Dollarama</h3></a><span class="distance">3.2 km</span><span class="storeid">2482435b-dcc2-41b5-8abe-02054f5c92b9</span><p class="address">3765 Sherwood Dr</p><p class="city-postal-code">Regina, SK S4R4A8</p><a class="directions" href="https://www.google.com/maps/dir//3765 Sherwood Dr Regina SK" data-label="3765 Sherwood Dr" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 546-2492" class="phone" data-label="306-546-2492" data-tel="+13065462492" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 546-2492</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-3765-sherwood-dr" data-label="3765 Sherwood Dr" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=TL&amp;storeid=683" class="btn btn-default btn-job">Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=683" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=683" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="89470121-6f88-444d-8441-708f21c61f0b"><div class="counter">5</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-3806-albert-st" data-label="3806 Albert St" target="_self"><h3>Dollarama</h3></a><span class="distance">3.5 km</span><span class="storeid">89470121-6f88-444d-8441-708f21c61f0b</span><p class="address">3806 Albert St</p><p class="city-postal-code">Regina, SK S4S 3R1</p><a class="directions" href="https://www.google.com/maps/dir//3806 Albert St Regina SK" data-label="3806 Albert St" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 761-1201" class="phone" data-label="306-761-1201" data-tel="+13067611201" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 761-1201</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-3806-albert-st" data-label="3806 Albert St" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=1178" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=1178" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="08c97586-af81-4ba2-b2c9-22dd8743b63d"><div class="counter">6</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-489-albert-st-n" data-label="489 Albert St N" target="_self"><h3>Dollarama</h3></a><span class="distance">3.9 km</span><span class="storeid">08c97586-af81-4ba2-b2c9-22dd8743b63d</span><p class="address">489 Albert St N</p><p class="city-postal-code">Regina, SK S4R3C3</p><a class="directions" href="https://www.google.com/maps/dir//489 Albert St N Regina SK" data-label="489 Albert St N" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Closed now.</span><br> Opening tomorrow at 11:00AM</p><div class="wrapper-copy"><div><a href="tel:(306) 525-0454" class="phone" data-label="306-525-0454" data-tel="+13065250454" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 525-0454</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-489-albert-st-n" data-label="489 Albert St N" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=669" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=669" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="6745f1b6-879b-488f-8a54-6743a8d9ec15"><div class="counter">7</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-2327-e-victoria-ave" data-label="2327 E Victoria Ave" target="_self"><h3>Dollarama</h3></a><span class="distance">4.8 km</span><span class="storeid">6745f1b6-879b-488f-8a54-6743a8d9ec15</span><p class="address">2327 E Victoria Ave</p><p class="city-postal-code">Regina, SK S4N1K5</p><a class="directions" href="https://www.google.com/maps/dir//2327 E Victoria Ave Regina SK" data-label="2327 E Victoria Ave" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 546-2725" class="phone" data-label="306-546-2725" data-tel="+13065462725" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 546-2725</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-2327-e-victoria-ave" data-label="2327 E Victoria Ave" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=572" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=572" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="07906fb3-fb7a-475e-89d5-cf5bc935e080"><div class="counter">8</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-4602-albert-st" data-label="4602 Albert St" target="_self"><h3>Dollarama</h3></a><span class="distance">4.8 km</span><span class="storeid">07906fb3-fb7a-475e-89d5-cf5bc935e080</span><p class="address">4602 Albert St</p><p class="city-postal-code">Regina, SK S4S6B4</p><a class="directions" href="https://www.google.com/maps/dir//4602 Albert St Regina SK" data-label="4602 Albert St" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 586-8929" class="phone" data-label="306-586-8929" data-tel="+13065868929" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 586-8929</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-4602-albert-st" data-label="4602 Albert St" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=728" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=728" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="042912fb-b4df-49d0-b5e7-da760151e828"><div class="counter">9</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-348-mccarthy-blvd-n" data-label="348 McCarthy Blvd N" target="_self"><h3>Dollarama</h3></a><span class="distance">5.1 km</span><span class="storeid">042912fb-b4df-49d0-b5e7-da760151e828</span><p class="address">348 McCarthy Blvd N</p><p class="city-postal-code">Regina, SK S4R7M2</p><a class="directions" href="https://www.google.com/maps/dir//348 McCarthy Blvd N Regina SK" data-label="348 McCarthy Blvd N" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 924-1932" class="phone" data-label="306-924-1932" data-tel="+13069241932" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 924-1932</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-348-mccarthy-blvd-n" data-label="348 McCarthy Blvd N" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=448" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=448" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="38706cec-8e27-4066-a22c-bd7ef21cc2f8"><div class="counter">10</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-4105-rochdale-blvd" data-label="4105 Rochdale Blvd" target="_self"><h3>Dollarama</h3></a><span class="distance">5.4 km</span><span class="storeid">38706cec-8e27-4066-a22c-bd7ef21cc2f8</span><p class="address">4105 Rochdale Blvd</p><p class="city-postal-code">Regina, SK S4X4P7</p><a class="directions" href="https://www.google.com/maps/dir//4105 Rochdale Blvd Regina SK" data-label="4105 Rochdale Blvd" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 522-2091" class="phone" data-label="306-522-2091" data-tel="+13065222091" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 522-2091</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-4105-rochdale-blvd" data-label="4105 Rochdale Blvd" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=TL&amp;storeid=703" class="btn btn-default btn-job">Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=703" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=703" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="d36a9c95-35c8-4545-9c80-45a5950a4706"><div class="counter">11</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-4825-gordon-rd" data-label="4825 Gordon Rd" target="_self"><h3>Dollarama</h3></a><span class="distance">5.6 km</span><span class="storeid">d36a9c95-35c8-4545-9c80-45a5950a4706</span><p class="address">4825 Gordon Rd</p><p class="city-postal-code">Regina, SK S4W0B7</p><a class="directions" href="https://www.google.com/maps/dir//4825 Gordon Rd Regina SK" data-label="4825 Gordon Rd" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 584-5994" class="phone" data-label="306-584-5994" data-tel="+13065845994" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 584-5994</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-4825-gordon-rd" data-label="4825 Gordon Rd" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=TL&amp;storeid=935" class="btn btn-default btn-job">Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=935" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=935" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="4380ae88-ed5d-49fa-ae3b-d8705684c28b"><div class="counter">12</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-2022-aurora-blvd" data-label="2022 Aurora Blvd." target="_self"><h3>Dollarama</h3></a><span class="distance">7.5 km</span><span class="storeid">4380ae88-ed5d-49fa-ae3b-d8705684c28b</span><p class="address">2022 Aurora Blvd.</p><p class="city-postal-code">Regina, SK S4V 3T7</p><a class="directions" href="https://www.google.com/maps/dir//2022 Aurora Blvd. Regina SK" data-label="2022 Aurora Blvd." target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 545-3031" class="phone" data-label="306-545-3031" data-tel="+13065453031" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 545-3031</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-2022-aurora-blvd" data-label="2022 Aurora Blvd." target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=TL&amp;storeid=1458" class="btn btn-default btn-job">Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=1458" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=1458" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div><div class="row" data-id="3bf0a9a6-c5e0-45c1-8420-5350b7d76d4e"><div class="counter">13</div><div class="text"><a class="details-link" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-3715-chuka-blvd" data-label="3715 Chuka Blvd" target="_self"><h3>Dollarama</h3></a><span class="distance">8.2 km</span><span class="storeid">3bf0a9a6-c5e0-45c1-8420-5350b7d76d4e</span><p class="address">3715 Chuka Blvd</p><p class="city-postal-code">Regina, SK S4V 3P7</p><a class="directions" href="https://www.google.com/maps/dir//3715 Chuka Blvd Regina SK" data-label="3715 Chuka Blvd" target="_blank">Get Directions to this <span class="text-nowrap">Store <i class="fa fa-chevron-right" aria-hidden="true"></i></span></a><p class="open-hours"><span class="highlight">Open</span> today until 9:00PM</p><div class="wrapper-copy"><div><a href="tel:(306) 569-7859" class="phone" data-label="306-569-7859" data-tel="+13065697859" data-country="CA"><span class="phone-text">Phone: </span><span class="phone-number">(306) 569-7859</span></a><a class="details-button btn btn-default" href="https://www.dollarama.com/en-CA/careers/locations/sk/regina-3715-chuka-blvd" data-label="3715 Chuka Blvd" target="_self">Job opportunities</a></div><div><div class="job-positions-block"><strong>Apply for in-store positions:</strong><br><a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=ATL&amp;storeid=1306" class="btn btn-default btn-job">Assistant Team Leader</a> <a href="https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&amp;storeid=1306" class="btn btn-default btn-job">Store Associate</a></div></div></div><hr></div></div></div>
        <div class="map-container expanded col-sm-7">
            <span class="hide-text">Hide Map</span>
            <div class="update-search-wrapper hidden-sm hidden-md hidden-lg"><div class="update-search-button">Search This Area</div></div>
            <div id="map" class="map mapboxgl-map">
            <div class="mapboxgl-canary" style="visibility: hidden;"></div><div class="mapboxgl-canvas-container mapboxgl-interactive mapboxgl-touch-drag-pan mapboxgl-touch-zoom-rotate"><canvas class="mapboxgl-canvas" tabindex="0" aria-label="Map" width="1192" height="1430" style="position: absolute; width: 542px; height: 650px;"></canvas><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="2102 11th Avenue" style="transform: translate(-50%, -50%) translate(225px, 353px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="514268a8-17ac-4c1d-8e8e-78c01d6daf1d">1</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="1230H Broad St" style="transform: translate(-50%, -50%) translate(233px, 325px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="148c6422-83c2-4b18-970c-9e45778a4b7e">2</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="921 A. Albert St" style="transform: translate(-50%, -50%) translate(213px, 311px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="92a90d60-875f-43a1-ac96-ebaf2e63a0e4">3</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="3765 Sherwood Dr" style="transform: translate(-50%, -50%) translate(174px, 272px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="2482435b-dcc2-41b5-8abe-02054f5c92b9">4</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="3806 Albert St" style="transform: translate(-50%, -50%) translate(208px, 467px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="89470121-6f88-444d-8441-708f21c61f0b">5</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="489 Albert St N" style="transform: translate(-50%, -50%) translate(218px, 242px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="08c97586-af81-4ba2-b2c9-22dd8743b63d">6</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="2327 E Victoria Ave" style="transform: translate(-50%, -50%) translate(358px, 368px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="6745f1b6-879b-488f-8a54-6743a8d9ec15">7</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="4602 Albert St" style="transform: translate(-50%, -50%) translate(208px, 507px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="07906fb3-fb7a-475e-89d5-cf5bc935e080">8</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="348 McCarthy Blvd N" style="transform: translate(-50%, -50%) translate(107px, 248px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="042912fb-b4df-49d0-b5e7-da760151e828">9</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="4105 Rochdale Blvd" style="transform: translate(-50%, -50%) translate(163px, 204px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="38706cec-8e27-4066-a22c-bd7ef21cc2f8">10</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="4825 Gordon Rd" style="transform: translate(-50%, -50%) translate(142px, 514px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="d36a9c95-35c8-4545-9c80-45a5950a4706">11</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="2022 Aurora Blvd." style="transform: translate(-50%, -50%) translate(441px, 368px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="4380ae88-ed5d-49fa-ae3b-d8705684c28b">12</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div><div class="marker mapboxgl-marker mapboxgl-marker-anchor-center" data-address="3715 Chuka Blvd" style="transform: translate(-50%, -50%) translate(439px, 467px);"><span style="position: absolute;width: 100%;padding-top: 4px;" data-id="3bf0a9a6-c5e0-45c1-8420-5350b7d76d4e">13</span><img src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker.svg" alt="dollarama marker" class="green"><img style="display:none;" src="https://www.dollarama.com/en-CA/locations/resources/images/dolla-marker-orange.svg" alt="dollarama marker" class="orange"></div></div><div class="mapboxgl-control-container"><div class="mapboxgl-ctrl-top-left"></div><div class="mapboxgl-ctrl-top-right"></div><div class="mapboxgl-ctrl-bottom-left"><div class="mapboxgl-ctrl" style="display: block;"><a class="mapboxgl-ctrl-logo" target="_blank" rel="noopener" href="https://www.mapbox.com/" aria-label="Mapbox logo"></a></div></div><div class="mapboxgl-ctrl-bottom-right"><div class="mapboxgl-ctrl mapboxgl-ctrl-attrib mapboxgl-compact"><div class="mapboxgl-ctrl-attrib-inner"><a href="https://www.mapbox.com/about/maps/" target="_blank" title="Mapbox" aria-label="Mapbox" role="listitem">© Mapbox</a> <a href="https://www.openstreetmap.org/about/" target="_blank" title="OpenStreetMap" aria-label="OpenStreetMap" role="listitem">© OpenStreetMap</a> <a class="mapbox-improve-map" href="https://apps.mapbox.com/feedback/?owner=mapbox&amp;id=streets-v11&amp;access_token=pk.eyJ1IjoidGJvb2RyYW0iLCJhIjoiY2p4cWVxaDRrMDA3dTNlbGp3MmY4MW16OCJ9.H-c1loygiF2kMyZT3N_eOQ" target="_blank" title="Improve this map" aria-label="Improve this map" role="listitem" rel="noopener">Improve this map</a></div></div></div></div></div>
        </div>
    </div>

</div>

    <script>
        var jobLink = "https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position={code}&storeid={storeId}";
    </script>






<footer class="footer-container"><footer id="footer" class="" role="contentinfo">

    <div class="container hidden-xs">
        <div class="row">
            <div class="col-sm-4">
                <div class="menu-header">
                    <p>Dollarama</p>

                    <ul class="menu list-unstyled"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1640"><a href="https://www.dollarama.com/en-CA/locations">Store Locator</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1189"><a href="https://www.dollarama.com/en-CA/corp/about-us">About Us</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1190"><a href="https://www.dollarama.com/en-CA/corp/careers">Career Opportunities</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1192"><a target="_blank" rel="noopener" href="https://www.dollarama.com/en-CA/corp/investor-relations">Investor Relations</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3403"><a href="https://www.dollarama.com/en-CA/corp/sustainability">Sustainability</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1191"><a href="https://www.dollarama.com/en-CA/corp/real-estate-partners">Real Estate Partners</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4568"><a href="https://www.dollarama.com/en-CA/legal-matters?origin=footer&amp;c1=dollarama&amp;c2=legal-matters&amp;clickedon=legal-matters">Legal matters</a></li>
</ul>                </div>
            </div>

            <div id="footer-col-2" class="col-sm-4 text-center">
                <div class="menu-header">
                    <p>Customer Service</p>
                    <ul class="menu list-unstyled"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1193"><a href="https://www.dollarama.com/en-CA/corp/accessibility-for-ontarians-with-disabilities-act">Accessibility Policy</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2409"><a href="https://www.dollarama.com/en-CA/corp/product-recalls">Product Recalls</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1194"><a href="https://www.dollarama.com/en-CA/corp/contact-us">Contact Us</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1892"><a href="https://www.dollarama.com/en-CA/FAQ/Website/Account-Registration">FAQ’s</a></li>
</ul>                </div>
            </div>

            <div id="footer-col-3" class="col-sm-4 text-right">
                <div class="menu-header">
                    <p>Shop</p>

                    <ul class="menu list-unstyled"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1196"><a href="https://www.dollarama.com/en-CA/">Shop Online</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1197"><a href="https://www.dollarama.com/en-CA/order-status">Check Order Status</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1913"><a href="https://www.dollarama.com/en-CA/Flat-Fee-Lookup">Shipping Fees</a></li>
</ul>                </div>
            </div>
        </div>
    </div>

    <div class="container visible-xs-block">
        <div class="row">
            <div class="footer-col-wrapper col-xs-12">
                <a class="menu-header collapsed" role="button" data-toggle="collapse" href="#col1" aria-expanded="false" aria-controls="col1">
                    <div class="pull-right">
                        <span class="glyphicon glyphicon-chevron-down"></span>
                        <span class="glyphicon glyphicon-chevron-up"></span>
                    </div>
                    Dollarama                </a>
                <div class="collapse" id="col1">
                    <ul class="menu list-unstyled"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1640"><a href="https://www.dollarama.com/en-CA/locations">Store Locator</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1189"><a href="https://www.dollarama.com/en-CA/corp/about-us">About Us</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1190"><a href="https://www.dollarama.com/en-CA/corp/careers">Career Opportunities</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1192"><a target="_blank" rel="noopener" href="https://www.dollarama.com/en-CA/corp/investor-relations">Investor Relations</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3403"><a href="https://www.dollarama.com/en-CA/corp/sustainability">Sustainability</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1191"><a href="https://www.dollarama.com/en-CA/corp/real-estate-partners">Real Estate Partners</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4568"><a href="https://www.dollarama.com/en-CA/legal-matters?origin=footer&amp;c1=dollarama&amp;c2=legal-matters&amp;clickedon=legal-matters">Legal matters</a></li>
</ul>                </div>
            </div>

            <div class="footer-col-wrapper col-xs-12">
                <a class="menu-header collapsed" role="button" data-toggle="collapse" href="#col2" aria-expanded="false" aria-controls="col2">
                    <div class="pull-right">
                        <span class="glyphicon glyphicon-chevron-down"></span>
                        <span class="glyphicon glyphicon-chevron-up"></span>
                    </div>
                    Customer Service                </a>
                <div class="collapse" id="col2">
                    <ul class="menu list-unstyled"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1193"><a href="https://www.dollarama.com/en-CA/corp/accessibility-for-ontarians-with-disabilities-act">Accessibility Policy</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2409"><a href="https://www.dollarama.com/en-CA/corp/product-recalls">Product Recalls</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1194"><a href="https://www.dollarama.com/en-CA/corp/contact-us">Contact Us</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1892"><a href="https://www.dollarama.com/en-CA/FAQ/Website/Account-Registration">FAQ’s</a></li>
</ul>                </div>
            </div>

            <div class="footer-col-wrapper col-xs-12">
                <a class="menu-header collapsed" role="button" data-toggle="collapse" href="#col3" aria-expanded="false" aria-controls="col3">
                    <div class="pull-right">
                        <span class="glyphicon glyphicon-chevron-down"></span>
                        <span class="glyphicon glyphicon-chevron-up"></span>
                    </div>
                    Shop                </a>
                <div class="collapse" id="col3">
                    <ul class="menu list-unstyled"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1196"><a href="https://www.dollarama.com/en-CA/">Shop Online</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1197"><a href="https://www.dollarama.com/en-CA/order-status">Check Order Status</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1913"><a href="https://www.dollarama.com/en-CA/Flat-Fee-Lookup">Shipping Fees</a></li>
</ul>                </div>
            </div>
        </div>
    </div>
</footer></footer>
<footer class="footer-bottom-container"><footer id="footer-bottom-nav" class="" role="">
    <div class="container">
        <div class="row">
            <div class="col-sm-6 sm-right">
                
            </div>
            <div class="col-sm-6">
                <p class="copyright inline">© Dollarama Inc. All rights reserved.</p>
            </div>
        </div>
    </div>
</footer><div id="flatfee-lookup-modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="FlatFeeLookup" aria-describedby="Modal dialog offering flat fee confirmation functionality">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-body row" style="padding-top: 0;">
                <button type="button" class="btn-link btn-lg pull-right" data-dismiss="modal" title="Close">
                    <img src="https://www.dollarama.com/en-CA/corp/wp-content/themes/dollarama2015/resources/images/x.gif" alt="close">
                </button>
                <iframe class="col-xs-12 text-center" src="https://www.dollarama.com/en-CA/corp/flat_fee/flat_fee_checkup_modal.php" height="420" id="flatfee"></iframe>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><div id="giftcard-modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="GiftcardLookup" aria-describedby="Modal dialog providing gift card balance verification steps">
    <div class="modal-dialog" role="document">
        <div class="modal-content ">
            <div class="modal-body row" style="padding-top: 0;">
                <div class="giftcard-modal-content text-center">
                    <button type="button" class="btn-link btn-lg pull-right" data-dismiss="modal" title="Close">
                        <img src="https://www.dollarama.com/en-CA/corp/wp-content/themes/dollarama2015/resources/images/x.gif" alt="close">
                    </button>
                    <div class="col-xs-12 text-center">
                        <img src="https://www.dollarama.com/en-CA/corp/wp-content/themes/dollarama2015/resources/images/giftcard/giftcards.png" alt="Giftcards">
                        <p style="font-size: 24px;">
                            Need to find the balance on your gift card?                            <br>
                            Please contact <a href="https://www.dollarama.com/en-CA/corp/contact-us">Customer Service</a>                        </p>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div></footer>

    

<div id="scripts">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <!--IE11 polyfills-->
    <script type="text/javascript" src="https://www.dollarama.com/en-CA/locations/js/bluebird.min.js"></script>
    <script type="text/javascript" src="https://www.dollarama.com/en-CA/locations/js/unorm.js"></script>
    <!--End IE11 polyfills-->
    <script type="text/javascript" src="https://www.dollarama.com/en-CA/careers/locations/js/dollarama-track.js"></script>
    <script type="text/javascript" src="https://www.dollarama.com/en-CA/careers/locations/js/dollarama.js"></script>
    <script type="text/javascript" src="https://www.dollarama.com/en-CA/locations/js/bootstrap.min.js"></script>
</div>

<script>

    $("footer.footer-container").load(jsResPrefix.value + "GetHeaderFooter #footer", function () {

    });
    $("footer.footer-bottom-container").load(jsResPrefix.value + "GetHeaderFooter #footer-bottom-nav, #flatfee-lookup-modal, #giftcard-modal", function () {
        var scripts = document.getElementById('scripts');
    });

</script>
    <script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/v2cb3a2ab87c5498db5ce7e6608cf55231689030342039" integrity="sha512-DI3rPuZDcpH/mSGyN22erN5QFnhl760f50/te7FTIYxodEF8jJnSFnfnmG/c+osmIQemvUrnBtxnMpNdzvx1/g==" data-cf-beacon="{&quot;rayId&quot;:&quot;7eafc344ca5522e8&quot;,&quot;token&quot;:&quot;8b2241104e78497f9bae8a1c6c21f115&quot;,&quot;version&quot;:&quot;2023.4.0&quot;,&quot;si&quot;:100}" crossorigin="anonymous"></script>

    

<iframe frameborder="0" scrolling="no" style="background-color: transparent; border: 0px; display: none;"></iframe><div id="GOOGLE_INPUT_CHEXT_FLAG" input="" input_stat="{&quot;tlang&quot;:true,&quot;tsbc&quot;:true,&quot;pun&quot;:true,&quot;mk&quot;:true,&quot;ss&quot;:true}" style="display: none;"></div><script id="ba_db_a_bibhbsjsonint" type="text/javascript" src="chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/js/jgi.js"></script><div id="ba_db_a_bibhbsin" style="color: initial; font: initial; font-palette: initial; font-synthesis: initial; forced-color-adjust: initial; text-orientation: initial; text-rendering: initial; -webkit-font-smoothing: initial; -webkit-locale: initial; -webkit-text-orientation: initial; -webkit-writing-mode: initial; writing-mode: initial; zoom: initial; accent-color: initial; place-content: initial; place-items: initial; place-self: initial; alignment-baseline: initial; animation-composition: initial; animation: initial; app-region: initial; appearance: initial; aspect-ratio: initial; backdrop-filter: initial; backface-visibility: initial; background: initial; background-blend-mode: initial; baseline-shift: initial; baseline-source: initial; block-size: initial; border-block: initial; border: initial; border-radius: initial; border-collapse: initial; border-end-end-radius: initial; border-end-start-radius: initial; border-inline: initial; border-start-end-radius: initial; border-start-start-radius: initial; inset: initial; box-shadow: initial; box-sizing: initial; break-after: initial; break-before: initial; break-inside: initial; buffered-rendering: initial; caption-side: initial; caret-color: initial; clear: initial; clip: initial; clip-path: initial; clip-rule: initial; color-interpolation: initial; color-interpolation-filters: initial; color-rendering: initial; color-scheme: initial; columns: initial; column-fill: initial; gap: initial; column-rule: initial; column-span: initial; contain: initial; contain-intrinsic-block-size: initial; contain-intrinsic-size: initial; contain-intrinsic-inline-size: initial; container: initial; content: initial; content-visibility: initial; counter-increment: initial; counter-reset: initial; counter-set: initial; cursor: initial; cx: initial; cy: initial; d: initial; display: initial; dominant-baseline: initial; empty-cells: initial; fill: initial; fill-opacity: initial; fill-rule: initial; filter: initial; flex: initial; flex-flow: initial; float: initial; flood-color: initial; flood-opacity: initial; grid: initial; grid-area: initial; height: initial; hyphenate-character: initial; hyphenate-limit-chars: initial; hyphens: initial; image-orientation: initial; image-rendering: initial; initial-letter: initial; inline-size: initial; inset-block: initial; inset-inline: initial; isolation: initial; letter-spacing: initial; lighting-color: initial; line-break: initial; list-style: initial; margin-block: initial; margin: initial; margin-inline: initial; marker: initial; mask: initial; mask-type: initial; math-depth: initial; math-shift: initial; math-style: initial; max-block-size: initial; max-height: initial; max-inline-size: initial; max-width: initial; min-block-size: initial; min-height: initial; min-inline-size: initial; min-width: initial; mix-blend-mode: initial; object-fit: initial; object-position: initial; object-view-box: initial; offset: initial; opacity: initial; order: initial; orphans: initial; outline: initial; outline-offset: initial; overflow-anchor: initial; overflow-clip-margin: initial; overflow-wrap: initial; overflow: initial; overscroll-behavior-block: initial; overscroll-behavior-inline: initial; overscroll-behavior: initial; padding-block: initial; padding: initial; padding-inline: initial; page: initial; page-orientation: initial; paint-order: initial; perspective: initial; perspective-origin: initial; pointer-events: initial; position: relative; quotes: initial; r: initial; resize: initial; rotate: initial; ruby-position: initial; rx: initial; ry: initial; scale: initial; scroll-behavior: initial; scroll-margin-block: initial; scroll-margin: initial; scroll-margin-inline: initial; scroll-padding-block: initial; scroll-padding: initial; scroll-padding-inline: initial; scroll-snap-align: initial; scroll-snap-stop: initial; scroll-snap-type: initial; scroll-timeline: initial; scrollbar-gutter: initial; shape-image-threshold: initial; shape-margin: initial; shape-outside: initial; shape-rendering: initial; size: initial; speak: initial; stop-color: initial; stop-opacity: initial; stroke: initial; stroke-dasharray: initial; stroke-dashoffset: initial; stroke-linecap: initial; stroke-linejoin: initial; stroke-miterlimit: initial; stroke-opacity: initial; stroke-width: initial; tab-size: initial; table-layout: initial; text-align: initial; text-align-last: initial; text-anchor: initial; text-combine-upright: initial; text-decoration: initial; text-decoration-skip-ink: initial; text-emphasis: initial; text-emphasis-position: initial; text-indent: initial; text-overflow: initial; text-shadow: initial; text-size-adjust: initial; text-transform: initial; text-underline-offset: initial; text-underline-position: initial; white-space: initial; touch-action: initial; transform: initial; transform-box: initial; transform-origin: initial; transform-style: initial; transition: initial; translate: initial; user-select: initial; vector-effect: initial; vertical-align: initial; view-timeline: initial; view-timeline-inset: initial; view-transition-name: initial; visibility: initial; border-spacing: initial; -webkit-box-align: initial; -webkit-box-decoration-break: initial; -webkit-box-direction: initial; -webkit-box-flex: initial; -webkit-box-ordinal-group: initial; -webkit-box-orient: initial; -webkit-box-pack: initial; -webkit-box-reflect: initial; -webkit-highlight: initial; -webkit-line-break: initial; -webkit-line-clamp: initial; -webkit-mask-box-image: initial; -webkit-mask: initial; -webkit-mask-composite: initial; -webkit-print-color-adjust: initial; -webkit-rtl-ordering: initial; -webkit-ruby-position: initial; -webkit-tap-highlight-color: initial; -webkit-text-combine: initial; -webkit-text-decorations-in-effect: initial; -webkit-text-fill-color: initial; -webkit-text-security: initial; -webkit-text-stroke: initial; -webkit-user-drag: initial; -webkit-user-modify: initial; widows: initial; width: initial; will-change: initial; word-break: initial; word-spacing: initial; x: initial; y: initial; z-index: 2147483647;"><style type="text/css">@font-face{font-family:"Roboto";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-100.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-100.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-100.ttf) format("truetype");font-style:normal;font-weight:100;font-display:swap}@font-face{font-family:"Roboto";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-300.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-300.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-300.ttf) format("truetype");font-style:normal;font-weight:300;font-display:swap}@font-face{font-family:"Roboto";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-400.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-400.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-400.ttf) format("truetype");font-style:normal;font-weight:400;font-display:swap}@font-face{font-family:"Roboto";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-500.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-500.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-500.ttf) format("truetype");font-style:normal;font-weight:500;font-display:swap}@font-face{font-family:"Roboto";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-700.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-700.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-700.ttf) format("truetype");font-style:normal;font-weight:700;font-display:swap}@font-face{font-family:"Roboto";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-900.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-900.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Roboto/roboto-900.ttf) format("truetype");font-style:normal;font-weight:900;font-display:swap}@font-face{font-family:"Rebond";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-400.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-400.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-400.ttf) format("truetype");font-style:normal;font-weight:400;font-display:swap}@font-face{font-family:"Rebond";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-500.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-500.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-500.ttf) format("truetype");font-style:normal;font-weight:500;font-display:swap}@font-face{font-family:"Rebond";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-600.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-600.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-600.ttf) format("truetype");font-style:normal;font-weight:600;font-display:swap}@font-face{font-family:"Rebond";src:url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-700.woff) format("woff"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-700.woff2) format("woff2"),url(chrome-extension://emalgedpdlghbkikiaeocoblajamonoh/fonts/Rebond/rebond-700.ttf) format("truetype");font-style:normal;font-weight:700;font-display:swap}</style><style type="text/css">#ba_db_a_bibhbsin div:empty {
          display: block !important;
        }#__wikibuy__ .__wikibuy.__onTop,body~div:not(#gdx-bubble-host),#piggyWrapper,#honeyContainer,#earny-root{position:absolute !important;z-index:100000 !important}body[data-shop-url="https://www.honeybum.com"] header>.header{z-index:99999}.mm-slideout{z-index:initial}.sorry-for-this__empty-styles{position:relative;z-index:10000}</style><div style="all: initial;"></div></div></body>


"""
# write a functione for below code to get store ids


def get_store_ids():
    pattern = r'storeid=(\d+)'  # regex pattern to find store ids
    matches = re.findall(pattern, html_source_code)  # find all matches
    matches = set(matches)  # convert the list to a set to get unique store IDs
    return matches


