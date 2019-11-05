(function(){
var app = angular.module("app",[]);
app.controller("AppCtrl", function($http){
var app = this;
app.message = "Am I Working?";
});
})();