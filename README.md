# nubo Framework
The Aim of this Automation framework is to provide an integrated framework as a service to end user, it’s an agile framework designed on Machine learning and can be easily integrated to Continuous Integration Tools for Continuous Testing.

Framework plans to integrate all the major opensource test automation frameworks into one framework and make it easy to use for end user. Current plan is to integrate test frameworks/tools like Tempest, Rally, Yardstick, TestON, Robot frameworks, 
	For Test Artifacts, the framework will integrate with SVN and git and for test scripts review in git it will be integrated with gerrit.
	For Issues tracking it will be integrated with Bugzilla.
	For Log Analysis, it will be integrated with ELK.
	Mysql will be the default database.
	Python scheduler(s) will be used to run test scripts on target environment, it will/should handle requests parallelly. User will have option to run test scripts at defined time and will/should have option to cancel/suspend running tasks.
In addition to supporting multiple frameworks integration, the current framework allows user to add test artifacts with much more easy way than others, user can speak/write plain English and it will get converted to test script.
