import streamlit as sl
import pyjokes
sl.header('Rattle joke generator')
sl.warning('WARNING!:THIS GENERATOR IS MOSTLY SUGGESTED FOR PROGRAMMERS')
if sl.button('Tell me a joke!'):
    sl.header(pyjokes.get_joke())