$(document).ready(function(){
//alert("Varun Kate")
var hashes = window.location.href.slice(window.location.href.indexOf('?'))
var i=hashes.indexOf(":")+1
var j=hashes.indexOf(",")
//alert(i+","+j)
//alert(hashes.slice(i,j))
var pid=hashes.slice(i,j)
       $.getJSON('/fetch_cart',function(data){
       //alert(data.data)
      var cart = JSON.parse(data.data)
      var key=Object.keys(cart)
      $('#shoppingcart').html(`(${key.length} Articals)&nbsp;&nbsp;&nbsp;`)
//      alert(key.includes(pid))
      if(key.includes(pid)){
      $('.addtocart').hide()
      $("#qtycomponents").show()
      $('#qty').html(cart[pid]['qty'])
      }
      else
      $("#qtycomponents").hide()
      })
$("#user-menu-button").click(function(){
   $('#dropdown').toggle()
})
$.getJSON("http://localhost:8000/fetch_all_user_categories",function(data){
    var htm=''
     data.data.map((item)=>{
//        alert(`<li><a href="http://localhost:8000/${item.categoryname}category/">${item.categoryname}</a></li>`)
        htm+=`<li><a href="http://localhost:8000/${item.categoryname}category/">${item.categoryname}</a></li>`
    })
    $('.mainmenu').html(htm)
       var htm=''
     data.data.map((item)=>{
        htm+=`<li><a href="">${item.categoryname}</a></li>`
    })
    $('.mobmainmenu').html(htm)
    })
 $.getJSON("http://localhost:8000/fetch_all_products",function(data){
   var htm=''
   var price
   var offerprice
   var save
   data.data.map((item)=>{
   if(item.offerprice>0)
   {
        price="<s style='color:red;'>"+item.price+"</s>"
        offerprice=item.offerprice
        save=item.price-item.offerprice
   }
   else
   {
        offerprice=item.price
        price="<div> </div>"
        save="<div> </div>"
   }
   var data=JSON.stringify(item)
    htm+=`<a href='http://localhost:8000/buyproduct?product=${data}'><div style="padding:5px; width:230px; display:flex; flex-direction:column; align-items: center; margin:10px;height:336px; border:1px solid #bdc3c7;box-shadow: 2px 3px #ecf0f1; border-radius: 10px;">
             <div>
                <img src="http://localhost:8000/static/${item.productimg}" style='width:150px; height:150px;'>
             </div>
             <div style="padding:10px;">
                  <div style="color:#34495e;width:200px; font-weight:bolder; text-align:left;">
                      ${item.productname} ${item.scname}
                  </div>
                  <div style=" width:200px; font-size:13px; text-align:left;">
                      <i>mkt:${item.bname}</i>
                  </div>
                  <div style=" width:200px; font-weight:bolder; text-align:left;">
                   Actual Price &#8377 ${price}
                  </div>
                  <div style=" width:200px; font-weight:bolder; text-align:left;">
                    Offer Price &#8377 ${offerprice}
                  </div>
                  <div style=" width:200px; font-weight:bolder; text-align:left;color:green;">
                   You Save &#8377 ${save}
                  </div>
             </div>
          </div></a>`
   })
   $('#productlist').html(htm)
 })
 $.getJSON("http://localhost:8000/fetch_all_user_subcategories_json",function(data){

    var him=0
    var htm=''
     data.data.map((item)=>{
     if(him<6)
     {
//     alert("jhxkjsh")
     htm+=`<div style="margin:5px;padding:10px;width:30%;background: #f5f6fa; height: 80px; border-radius: 10px; display: flex;flex-direction: row">`
     htm+=`<div style="padding: 5px"><img src='/static/${item.subcategoryicon}' width="50px"></div>`
     htm+=`<div style="display:flex; flex-direction: column;"><div style="font-weight:bold; padding: 5px">${item.subcategoryname}</div><div style="color: green;">Save upto 15%</div></div>`
     htm+=`</div>`
     him++;
     $('#subcategorylist').html(htm)
     }
     })
 })
 $('.plus').click(function(){
    var v=$('#qty').html()
//    alert($('#qty').html())
    if(v<=4)
    v++
    $('#qty').html(v)
    cartContainer($(this).attr('product'),$('#qty').html())
 })
 $('.minus').click(function(){
    var v=$('#qty').html()
//    alert($('#qty').html())
    if(v>0)
    {v--
//    alert(v)
    }
    if(v==0)
    {
       $(".addtocart").show()
       $("#qtycomponents").hide()
       RemoveCartContainer($(this).attr('productid'))
    }
    else
    {
       $('#qty').html(v)
      cartContainer($(this).attr('product'),$('#qty').html())
    }
 })

 $(".addtocart").click(function(){
   $(".addtocart").hide()
   $("#qtycomponents").show()
   $('#qty').html(1)
   cartContainer($(this).attr('product'),$('#qty').html())
 })
 function cartContainer(product,qty){
      $.getJSON('/add_to_cart',{'product':product,'qty':qty},function(data){
//      alert(JSON.stringify(data.data))
      var cart=JSON.parse(data.data)
      var key=Object.keys(cart)
      $('#shoppingcart').html(`(${key.length} Articals)&nbsp;&nbsp;&nbsp;`)
      })
 }
 function RemoveCartContainer(productid){
     $.getJSON('/remove_from_cart',{'productid':productid},function(data){
     alert("Removed Successfully from Cart")
     var cart=JSON.parse(data.data)
     var key=Object.keys(cart)
     $('#shoppingcart').html(`(${key.length} Articals)&nbsp;&nbsp;&nbsp;`)
     })
 }
})
function call()
{
   if(cdpwd.value==ccdpwd.value)
   {img.src="/static/tick.png"
//   alert("tick")
   }
   else
   {img.src="/static/cross.png"
//   alert("cross")
   }
}
function eye()
{
  if(cdpwd.type=="password")
  {
    cdpwd.type="text"
    eyeimg.src="/static/open.png"
  }
  else
  {
    cdpwd.type="password"
    eyeimg.src="/static/close.png"
  }
}
