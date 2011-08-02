/* 

	Image Link, multistyle version
	written by Alen Grakalic, provided by Css Globe (cssglobe.com)
	please visit http://cssglobe.com/post/1238/style-your-image-links for more info
	
*/

this.imagelink = function(){
	
	// CONFIG
	
	
	// with multistyle version of this script 
	// you can apply various styles to various images on site
	// the style "groups" consist of 3 elements:
	// 1. css class of images that you wish to apply style to
	// 2. css class that defines how span that covers the image is styled by default
	// 3. css class that defines how span that covers the image is styled when rolled over 
	//
	// use as many varioations as you want, just set the css class to images in html 

	
	// [image css class, covering span default css class, covering span mouseover css class]
	var arr = [			   			  				
				["image1", "", "imageOver"],
				["image2", "imageOut2", "imageOver2"],
				["image3", "", "imageOver3"],
				["image4", "", "imageOver4"],
				["image5", "", "imageOver5"]
			  ];
			
	// END CONFIG
	
	for (var x=0;x<arr.length;x++){
		
		var a = document.getElementsByTagName("a");
		for (var i=0;i<a.length;i++){
			var img = a[i].getElementsByTagName("img");		
			for (var j=0;j<img.length;j++){			
				if(img[j].className == arr[x][0] || arr[x][0] == ""){
					a[i].style.position = "static";						 
					if(a[i].getElementsByTagName("span").length > 0) a[i].removeChild(a[i].getElementsByTagName("span")[0]);
					var span = document.createElement("span");	
					var image = img[j];
					span.style.position = "absolute";
					span.style.top = image.offsetTop + "px";
					span.style.left = image.offsetLeft + "px";
					span.style.width = image.offsetWidth + "px";
					span.style.height = image.offsetHeight + "px";
					span.style.cursor = "pointer";
					span.out = span.className = arr[x][1];
					span.over = arr[x][2];
					span.a = img[j].a = a[i];	
					span.j = img[j].j = j;					
					a[i]["span" + j] = span;					
					span.onmouseover = img[j].onmouseover = function(){ 
						this.a["span" + this.j].className = this.a["span" + this.j].over;
					};
					span.onmouseout = img[j].onmouseout = function(){
						this.a["span" + this.j].className = this.a["span" + this.j].out;
					};
					a[i].appendChild(span);							
				};		
			};	
		};
		
	};
};



// script initiates on page load. 

this.addEvent = function(obj,type,fn){
	if(obj.attachEvent){
		obj['e'+type+fn] = fn;
		obj[type+fn] = function(){obj['e'+type+fn](window.event );}
		obj.attachEvent('on'+type, obj[type+fn]);
	} else {
		obj.addEventListener(type,fn,false);
	};
};
addEvent(window,"load",imagelink);
addEvent(window,"resize",imagelink);