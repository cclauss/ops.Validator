/**
 * Created by pm.verdugo@dit.upm.es on 12/05/2016.
 */
define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        config = require('config'),
        Recipe = require('models/RecipeModel'),
        basicauth = require('bbbasicauth'),
        bbsel = require('bbselect');

    return Backbone.Collection.extend({
        url: config.api_url + '/recipes/',
        model: Recipe,

        initialize: function (credentials, models, options) {
            this.get_remote(credentials);
            Backbone.Select.Many.applyTo(this, models, options);
        },

        get_remote: function (credentials) {
            console.log("Fetching Recipes...");
            this.credentials = credentials;
            this.fetch({reset: true});
        }
    });
});