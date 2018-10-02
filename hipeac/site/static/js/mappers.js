var linkTransform = function (items) {
    var output = {};
    _.each(items, function(obj){
        output[obj.type] = obj.url;
    });
    return output;
};

var mapper = function () {
    return {
        base: function (items) {
            return items.map(function (obj) {
                obj.q = '';
                return obj;
            });
        },
        articles: function (items) {
            return items.map(function (obj) {
                obj.markedExcerpt = marked(obj.excerpt);
                return obj;
            });
        },
        events: function (items) {
            var sessionsMapper = this.sessions;
            return items.map(function (obj) {
                obj.markedTravelInfo = (obj.travel_info) ? marked(obj.travel_info) : '';
                obj.registrations_round = (obj.registrations_count)
                    ? Math.floor(obj.registrations_count / 10) * 10
                    : 0;
                obj.links = linkTransform(obj.links);
                obj.href = obj.redirect_url || obj.href;
                obj.past = moment().isAfter(obj.end_date);
                obj.dates = [
                    moment(obj.start_date).format('MMMM D'),
                    moment(obj.end_date).format('D, YYYY'),
                ].join('-');
                if (obj.sessions) {
                    obj.sessions = sessionsMapper(obj.sessions);
                }
                return obj;
            });
        },
        institutions: function (items) {
            return items.map(function (obj) {
                obj.links = linkTransform(obj.links);
                obj.q = '';
                return obj;
            });
        },
        jobs: function (items) {
            return items.map(function (obj) {
                obj.careerLevelIds = _.pluck(obj.career_levels, 'id');
                obj.topicIds = _.pluck(obj.topics, 'id');
                obj.typeId = obj.employment_type.id;
                obj.internship = obj.employment_type.id == INTERNSHIP;
                obj.q = [
                    (obj.internship) ? 'internships' : '',
                    obj.title,
                    (obj.institution) ? obj.institution.name : '',
                    (obj.project) ? obj.project.acronym : '',
                    (obj.project) ? obj.project.name : '',
                    (obj.country) ? obj.country.name : '',
                    obj.city,
                    obj.keywords.join(' '),
                    _.map(obj.application_areas, function (o) { return o.value; }).join(' '),
                    _.map(obj.topics, function (o) { return o.value; }).join(' ')
                ].join(' ').toLowerCase();
                return obj;
            });
        },
        projects: function (items) {
            return items.map(function (obj) {
                obj.links = linkTransform(obj.links);
                obj.topicIds = _.pluck(obj.topics, 'id');
                obj.q = [
                    obj.acronym,
                    obj.name,
                    _.map(obj.application_areas, function (o) { return o.value; }).join(' '),
                    _.map(obj.topics, function (o) { return o.value; }).join(' ')
                ].join(' ').toLowerCase();
                return obj;
            });
        },
        sessions: function (items) {
            return items.map(function (obj) {
                obj.markedSummary = (obj.summary) ? marked(obj.summary) : '';
                obj.startAt = obj.start_at.substring(0, 5);
                obj.endAt = obj.end_at.substring(0, 5);
                obj.q = [
                    obj.title
                ].join(' ').toLowerCase();;
                return obj;
            });
        },
        visions: function (items) {
            return items.map(function (obj) {
                obj.markedIntroduction = marked(obj.introduction);
                obj.markedSummary = marked(obj.summary);
                obj.q = '';
                return obj;
            });
        }
    };
};
