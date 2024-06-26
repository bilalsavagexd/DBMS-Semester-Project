toc.dat                                                                                             0000600 0004000 0002000 00000017625 14617167101 0014456 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP   ,    '        	        |            Library_Management_System    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                     1262    16983    Library_Management_System    DATABASE     �   CREATE DATABASE "Library_Management_System" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
 +   DROP DATABASE "Library_Management_System";
                postgres    false         �            1259    17240    books    TABLE     �   CREATE TABLE public.books (
    book_id integer NOT NULL,
    title character varying(255) NOT NULL,
    author character varying(255),
    edition integer,
    copies integer
);
    DROP TABLE public.books;
       public         heap    postgres    false         �            1259    17239    books_book_id_seq    SEQUENCE     �   CREATE SEQUENCE public.books_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.books_book_id_seq;
       public          postgres    false    218                    0    0    books_book_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.books_book_id_seq OWNED BY public.books.book_id;
          public          postgres    false    217         �            1259    17249    transactions    TABLE     |  CREATE TABLE public.transactions (
    transaction_id integer NOT NULL,
    user_regno integer,
    book_id integer,
    transaction_type character varying(10),
    transaction_date date,
    return_date date,
    CONSTRAINT transactions_transaction_type_check CHECK (((transaction_type)::text = ANY ((ARRAY['issue'::character varying, 'return'::character varying])::text[])))
);
     DROP TABLE public.transactions;
       public         heap    postgres    false         �            1259    17248    transactions_transaction_id_seq    SEQUENCE     �   CREATE SEQUENCE public.transactions_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.transactions_transaction_id_seq;
       public          postgres    false    220                    0    0    transactions_transaction_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.transactions_transaction_id_seq OWNED BY public.transactions.transaction_id;
          public          postgres    false    219         �            1259    17231    user_details    TABLE     �   CREATE TABLE public.user_details (
    user_regno integer NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255)
);
     DROP TABLE public.user_details;
       public         heap    postgres    false         �            1259    17230    user_details_user_regno_seq    SEQUENCE     �   CREATE SEQUENCE public.user_details_user_regno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.user_details_user_regno_seq;
       public          postgres    false    216                    0    0    user_details_user_regno_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.user_details_user_regno_seq OWNED BY public.user_details.user_regno;
          public          postgres    false    215         [           2604    17243    books book_id    DEFAULT     n   ALTER TABLE ONLY public.books ALTER COLUMN book_id SET DEFAULT nextval('public.books_book_id_seq'::regclass);
 <   ALTER TABLE public.books ALTER COLUMN book_id DROP DEFAULT;
       public          postgres    false    217    218    218         \           2604    17252    transactions transaction_id    DEFAULT     �   ALTER TABLE ONLY public.transactions ALTER COLUMN transaction_id SET DEFAULT nextval('public.transactions_transaction_id_seq'::regclass);
 J   ALTER TABLE public.transactions ALTER COLUMN transaction_id DROP DEFAULT;
       public          postgres    false    220    219    220         Z           2604    17234    user_details user_regno    DEFAULT     �   ALTER TABLE ONLY public.user_details ALTER COLUMN user_regno SET DEFAULT nextval('public.user_details_user_regno_seq'::regclass);
 F   ALTER TABLE public.user_details ALTER COLUMN user_regno DROP DEFAULT;
       public          postgres    false    215    216    216         �          0    17240    books 
   TABLE DATA           H   COPY public.books (book_id, title, author, edition, copies) FROM stdin;
    public          postgres    false    218       4856.dat �          0    17249    transactions 
   TABLE DATA           |   COPY public.transactions (transaction_id, user_regno, book_id, transaction_type, transaction_date, return_date) FROM stdin;
    public          postgres    false    220       4858.dat �          0    17231    user_details 
   TABLE DATA           ?   COPY public.user_details (user_regno, name, email) FROM stdin;
    public          postgres    false    216       4854.dat            0    0    books_book_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.books_book_id_seq', 1, true);
          public          postgres    false    217                    0    0    transactions_transaction_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.transactions_transaction_id_seq', 1, false);
          public          postgres    false    219                    0    0    user_details_user_regno_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.user_details_user_regno_seq', 1, false);
          public          postgres    false    215         a           2606    17247    books books_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);
 :   ALTER TABLE ONLY public.books DROP CONSTRAINT books_pkey;
       public            postgres    false    218         c           2606    17255    transactions transactions_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (transaction_id);
 H   ALTER TABLE ONLY public.transactions DROP CONSTRAINT transactions_pkey;
       public            postgres    false    220         _           2606    17238    user_details user_details_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (user_regno);
 H   ALTER TABLE ONLY public.user_details DROP CONSTRAINT user_details_pkey;
       public            postgres    false    216         d           2606    17261 &   transactions transactions_book_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(book_id);
 P   ALTER TABLE ONLY public.transactions DROP CONSTRAINT transactions_book_id_fkey;
       public          postgres    false    220    4705    218         e           2606    17256 )   transactions transactions_user_regno_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_user_regno_fkey FOREIGN KEY (user_regno) REFERENCES public.user_details(user_regno);
 S   ALTER TABLE ONLY public.transactions DROP CONSTRAINT transactions_user_regno_fkey;
       public          postgres    false    220    4703    216                                                                                                                   4856.dat                                                                                            0000600 0004000 0002000 00000000070 14617167101 0014261 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	The Song of Ice and Fire	George R.R. Martin	2	10
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                        4858.dat                                                                                            0000600 0004000 0002000 00000000005 14617167101 0014261 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4854.dat                                                                                            0000600 0004000 0002000 00000000005 14617167101 0014255 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           restore.sql                                                                                         0000600 0004000 0002000 00000015641 14617167101 0015377 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
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
    book_id integer NOT NULL,
    title character varying(255) NOT NULL,
    author character varying(255),
    edition integer,
    copies integer
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Name: books_book_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.books_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.books_book_id_seq OWNER TO postgres;

--
-- Name: books_book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.books_book_id_seq OWNED BY public.books.book_id;


--
-- Name: transactions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transactions (
    transaction_id integer NOT NULL,
    user_regno integer,
    book_id integer,
    transaction_type character varying(10),
    transaction_date date,
    return_date date,
    CONSTRAINT transactions_transaction_type_check CHECK (((transaction_type)::text = ANY ((ARRAY['issue'::character varying, 'return'::character varying])::text[])))
);


ALTER TABLE public.transactions OWNER TO postgres;

--
-- Name: transactions_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transactions_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.transactions_transaction_id_seq OWNER TO postgres;

--
-- Name: transactions_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transactions_transaction_id_seq OWNED BY public.transactions.transaction_id;


--
-- Name: user_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_details (
    user_regno integer NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255)
);


ALTER TABLE public.user_details OWNER TO postgres;

--
-- Name: user_details_user_regno_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_details_user_regno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_details_user_regno_seq OWNER TO postgres;

--
-- Name: user_details_user_regno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_details_user_regno_seq OWNED BY public.user_details.user_regno;


--
-- Name: books book_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books ALTER COLUMN book_id SET DEFAULT nextval('public.books_book_id_seq'::regclass);


--
-- Name: transactions transaction_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions ALTER COLUMN transaction_id SET DEFAULT nextval('public.transactions_transaction_id_seq'::regclass);


--
-- Name: user_details user_regno; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_details ALTER COLUMN user_regno SET DEFAULT nextval('public.user_details_user_regno_seq'::regclass);


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.books (book_id, title, author, edition, copies) FROM stdin;
\.
COPY public.books (book_id, title, author, edition, copies) FROM '$$PATH$$/4856.dat';

--
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transactions (transaction_id, user_regno, book_id, transaction_type, transaction_date, return_date) FROM stdin;
\.
COPY public.transactions (transaction_id, user_regno, book_id, transaction_type, transaction_date, return_date) FROM '$$PATH$$/4858.dat';

--
-- Data for Name: user_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_details (user_regno, name, email) FROM stdin;
\.
COPY public.user_details (user_regno, name, email) FROM '$$PATH$$/4854.dat';

--
-- Name: books_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.books_book_id_seq', 1, true);


--
-- Name: transactions_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transactions_transaction_id_seq', 1, false);


--
-- Name: user_details_user_regno_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_details_user_regno_seq', 1, false);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);


--
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (transaction_id);


--
-- Name: user_details user_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (user_regno);


--
-- Name: transactions transactions_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(book_id);


--
-- Name: transactions transactions_user_regno_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_user_regno_fkey FOREIGN KEY (user_regno) REFERENCES public.user_details(user_regno);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               