angular.module('mwl.calendar.docs', ['mwl.calendar', 'ngAnimate', 'ui.bootstrap', 'colorpicker.module']);
angular
  .module('mwl.calendar.docs') //you will need to declare your module with the dependencies ['mwl.calendar', 'ui.bootstrap', 'ngAnimate']
  .controller('KitchenSinkCtrl', function(moment, alert, calendarConfig, $http) {

    var vm = this;

    //Variables calendario
    vm.calendarView = 'month';
    vm.viewDate = new Date();
    var actions = [{
      label: '<i class=\'glyphicon glyphicon-pencil\'></i>',
      onClick: function(args) {
        alert.show('Edited', args.calendarEvent);
      }
    }, {
      label: '<i class=\'glyphicon glyphicon-remove\'></i>',
      onClick: function(args) {
        alert.show('Deleted', args.calendarEvent);
      }
    }];
    vm.events = [];
    vm.cellIsOpen = true;

    vm.getParrilla = function(){
      $http({
        method: 'GET',
        url: 'http://elbosquestereo.com/get_parrilla/'
        }).then(function successCallback(response) {
          response.data.forEach(parrilla => {
            vm.events.push({
              title: parrilla.nombre,
              startsAt: new Date(parrilla.fecha_inicio),
              endsAt: new Date(parrilla.fecha_final),
              color: calendarConfig.colorTypes.important,
              draggable: false,
              resizable: false
            });
          });
        //console.log(response);
        // this callback will be called asynchronously
        // when the response is available
        }, function errorCallback(response) {
          alert('Error obteniendo información de parrilla');
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        });
    }
    
    vm.getParrilla();

    vm.addEvent = function() {
      vm.events.push({
        title: 'New event',
        startsAt: moment().startOf('day').toDate(),
        endsAt: moment().endOf('day').toDate(),
        color: calendarConfig.colorTypes.important,
        draggable: true,
        resizable: true
      });
      console.log(JSON.stringify(vm.events));
    };

    vm.eventClicked = function(event) {
      alert.show('Clicked', event);
    };

    vm.eventEdited = function(event) {
      alert.show('Edited', event);
    };

    vm.eventDeleted = function(event) {
      alert.show('Deleted', event);
    };

    vm.eventTimesChanged = function(event) {
      alert.show('Dropped or resized', event);
    };

    vm.toggle = function($event, field, event) {
      $event.preventDefault();
      $event.stopPropagation();
      event[field] = !event[field];
    };

    vm.timespanClicked = function(date, cell) {

      if (vm.calendarView === 'month') {
        if ((vm.cellIsOpen && moment(date).startOf('day').isSame(moment(vm.viewDate).startOf('day'))) || cell.events.length === 0 || !cell.inMonth) {
          vm.cellIsOpen = false;
        } else {
          vm.cellIsOpen = true;
          vm.viewDate = date;
        }
      } else if (vm.calendarView === 'year') {
        if ((vm.cellIsOpen && moment(date).startOf('month').isSame(moment(vm.viewDate).startOf('month'))) || cell.events.length === 0) {
          vm.cellIsOpen = false;
        } else {
          vm.cellIsOpen = true;
          vm.viewDate = date;
        }
      }

    };

  });

/**

[
  {
    "title":"New event",
    "startsAt":"2018-05-29T05:00:00.000Z",
    "endsAt":"2018-05-30T04:59:59.999Z",
    "color":
      {
        "primary":"#ad2121",
        "secondary":"#fae3e3"
      },
    "draggable":true,
    "resizable":true
  }
]

**/