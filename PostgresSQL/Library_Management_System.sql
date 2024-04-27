toc.dat                                                                                             0000600 0004000 0002000 00000010564 14613152104 0014442 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP   $                     |            Library_Management_System    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         �           1262    16983    Library_Management_System    DATABASE     �   CREATE DATABASE "Library_Management_System" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
 +   DROP DATABASE "Library_Management_System";
                postgres    false         �            1259    17022    books    TABLE     �   CREATE TABLE public.books (
    book_id character varying(255) NOT NULL,
    book_title character varying(255),
    author character varying(255),
    edition integer,
    copies integer
);
    DROP TABLE public.books;
       public         heap    postgres    false         �            1259    17029    issue    TABLE     �   CREATE TABLE public.issue (
    user_regno integer NOT NULL,
    book_id character varying(255),
    book_title character varying(255) NOT NULL,
    author character varying(255),
    issue_date date,
    return_date date
);
    DROP TABLE public.issue;
       public         heap    postgres    false         �            1259    17036    return    TABLE     �   CREATE TABLE public.return (
    user_regno integer,
    book_id character varying(255),
    book_title character varying(255) NOT NULL,
    author character varying(255),
    issue_date date,
    return_date date
);
    DROP TABLE public.return;
       public         heap    postgres    false         �            1259    17041    user_details    TABLE     �   CREATE TABLE public.user_details (
    user_regno integer NOT NULL,
    name character varying(255) NOT NULL,
    password character varying(255)
);
     DROP TABLE public.user_details;
       public         heap    postgres    false         �          0    17022    books 
   TABLE DATA           M   COPY public.books (book_id, book_title, author, edition, copies) FROM stdin;
    public          postgres    false    215       4850.dat �          0    17029    issue 
   TABLE DATA           a   COPY public.issue (user_regno, book_id, book_title, author, issue_date, return_date) FROM stdin;
    public          postgres    false    216       4851.dat �          0    17036    return 
   TABLE DATA           b   COPY public.return (user_regno, book_id, book_title, author, issue_date, return_date) FROM stdin;
    public          postgres    false    217       4852.dat �          0    17041    user_details 
   TABLE DATA           B   COPY public.user_details (user_regno, name, password) FROM stdin;
    public          postgres    false    218       4853.dat \           2606    17028    books books_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);
 :   ALTER TABLE ONLY public.books DROP CONSTRAINT books_pkey;
       public            postgres    false    215         ^           2606    17035    issue issue_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.issue
    ADD CONSTRAINT issue_pkey PRIMARY KEY (user_regno);
 :   ALTER TABLE ONLY public.issue DROP CONSTRAINT issue_pkey;
       public            postgres    false    216         `           2606    17049 &   user_details user_details_password_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.user_details
    ADD CONSTRAINT user_details_password_key UNIQUE (password);
 P   ALTER TABLE ONLY public.user_details DROP CONSTRAINT user_details_password_key;
       public            postgres    false    218         b           2606    17047    user_details user_details_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (user_regno);
 H   ALTER TABLE ONLY public.user_details DROP CONSTRAINT user_details_pkey;
       public            postgres    false    218                                                                                                                                                    4850.dat                                                                                            0000600 0004000 0002000 00000000005 14613152104 0014242 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4851.dat                                                                                            0000600 0004000 0002000 00000000005 14613152104 0014243 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4852.dat                                                                                            0000600 0004000 0002000 00000000005 14613152104 0014244 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4853.dat                                                                                            0000600 0004000 0002000 00000000005 14613152104 0014245 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           restore.sql                                                                                         0000600 0004000 0002000 00000010663 14613152104 0015367 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "Library_Management_System";
--
-- Name: Library_Management_System; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "Library_Management_System" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';


ALTER DATABASE "Library_Management_System" OWNER TO postgres;

\connect "Library_Management_System"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.books (
    book_id character varying(255) NOT NULL,
    book_title character varying(255),
    author character varying(255),
    edition integer,
    copies integer
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Name: issue; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.issue (
    user_regno integer NOT NULL,
    book_id character varying(255),
    book_title character varying(255) NOT NULL,
    author character varying(255),
    issue_date date,
    return_date date
);


ALTER TABLE public.issue OWNER TO postgres;

--
-- Name: return; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.return (
    user_regno integer,
    book_id character varying(255),
    book_title character varying(255) NOT NULL,
    author character varying(255),
    issue_date date,
    return_date date
);


ALTER TABLE public.return OWNER TO postgres;

--
-- Name: user_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_details (
    user_regno integer NOT NULL,
    name character varying(255) NOT NULL,
    password character varying(255)
);


ALTER TABLE public.user_details OWNER TO postgres;

--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.books (book_id, book_title, author, edition, copies) FROM stdin;
\.
COPY public.books (book_id, book_title, author, edition, copies) FROM '$$PATH$$/4850.dat';

--
-- Data for Name: issue; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.issue (user_regno, book_id, book_title, author, issue_date, return_date) FROM stdin;
\.
COPY public.issue (user_regno, book_id, book_title, author, issue_date, return_date) FROM '$$PATH$$/4851.dat';

--
-- Data for Name: return; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.return (user_regno, book_id, book_title, author, issue_date, return_date) FROM stdin;
\.
COPY public.return (user_regno, book_id, book_title, author, issue_date, return_date) FROM '$$PATH$$/4852.dat';

--
-- Data for Name: user_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_details (user_regno, name, password) FROM stdin;
\.
COPY public.user_details (user_regno, name, password) FROM '$$PATH$$/4853.dat';

--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);


--
-- Name: issue issue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.issue
    ADD CONSTRAINT issue_pkey PRIMARY KEY (user_regno);


--
-- Name: user_details user_details_password_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_details
    ADD CONSTRAINT user_details_password_key UNIQUE (password);


--
-- Name: user_details user_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (user_regno);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             