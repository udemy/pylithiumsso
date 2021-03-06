from setuptools import setup

setup(
   name="pylithiumsso",
   version="0.2.2",
   description="Python Client for Lithium SSO Integration",
   author="Alex Milstead",
   author_email="amilstead@jawbone.com",
   package_dir={"": "src"},
   packages = ["pylithium"],
   py_modules=["pylithium.client"],
   license="MIT",
   url="https://github.com/jawbone/pylithiumsso",
   test_suite='nose.collector',
   tests_require=["nose==1.2.1"],
   install_requires=["pycrypto>=2.6"]
)
