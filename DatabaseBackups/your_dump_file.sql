--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5
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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: storage_grids; Type: TABLE; Schema: public; Owner: default
--

CREATE TABLE public.storage_grids (
    id integer NOT NULL,
    name character varying,
    description text,
    row_count integer NOT NULL,
    column_count integer NOT NULL,
    image character varying,
    storage_place_id integer
);


ALTER TABLE public.storage_grids OWNER TO "default";

--
-- Name: storage_grids_id_seq; Type: SEQUENCE; Schema: public; Owner: default
--

CREATE SEQUENCE public.storage_grids_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.storage_grids_id_seq OWNER TO "default";

--
-- Name: storage_grids_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: default
--

ALTER SEQUENCE public.storage_grids_id_seq OWNED BY public.storage_grids.id;


--
-- Name: storage_places; Type: TABLE; Schema: public; Owner: default
--

CREATE TABLE public.storage_places (
    id integer NOT NULL,
    name character varying NOT NULL,
    description text,
    image character varying
);


ALTER TABLE public.storage_places OWNER TO "default";

--
-- Name: storage_places_id_seq; Type: SEQUENCE; Schema: public; Owner: default
--

CREATE SEQUENCE public.storage_places_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.storage_places_id_seq OWNER TO "default";

--
-- Name: storage_places_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: default
--

ALTER SEQUENCE public.storage_places_id_seq OWNED BY public.storage_places.id;


--
-- Name: storage_units; Type: TABLE; Schema: public; Owner: default
--

CREATE TABLE public.storage_units (
    id integer NOT NULL,
    name character varying NOT NULL,
    description text,
    image character varying,
    storage_place_id integer,
    storage_grid_id integer,
    storage_grid_row integer NOT NULL,
    storage_grid_column integer NOT NULL
);


ALTER TABLE public.storage_units OWNER TO "default";

--
-- Name: storage_units_id_seq; Type: SEQUENCE; Schema: public; Owner: default
--

CREATE SEQUENCE public.storage_units_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.storage_units_id_seq OWNER TO "default";

--
-- Name: storage_units_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: default
--

ALTER SEQUENCE public.storage_units_id_seq OWNED BY public.storage_units.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: default
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying,
    password character varying,
    email character varying
);


ALTER TABLE public.users OWNER TO "default";

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: default
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO "default";

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: default
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: storage_grids id; Type: DEFAULT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_grids ALTER COLUMN id SET DEFAULT nextval('public.storage_grids_id_seq'::regclass);


--
-- Name: storage_places id; Type: DEFAULT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_places ALTER COLUMN id SET DEFAULT nextval('public.storage_places_id_seq'::regclass);


--
-- Name: storage_units id; Type: DEFAULT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_units ALTER COLUMN id SET DEFAULT nextval('public.storage_units_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: storage_grids; Type: TABLE DATA; Schema: public; Owner: default
--

COPY public.storage_grids (id, name, description, row_count, column_count, image, storage_place_id) FROM stdin;
\.


--
-- Data for Name: storage_places; Type: TABLE DATA; Schema: public; Owner: default
--

COPY public.storage_places (id, name, description, image) FROM stdin;
\.


--
-- Data for Name: storage_units; Type: TABLE DATA; Schema: public; Owner: default
--

COPY public.storage_units (id, name, description, image, storage_place_id, storage_grid_id, storage_grid_row, storage_grid_column) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: default
--

COPY public.users (id, username, password, email) FROM stdin;
\.


--
-- Name: storage_grids_id_seq; Type: SEQUENCE SET; Schema: public; Owner: default
--

SELECT pg_catalog.setval('public.storage_grids_id_seq', 1, false);


--
-- Name: storage_places_id_seq; Type: SEQUENCE SET; Schema: public; Owner: default
--

SELECT pg_catalog.setval('public.storage_places_id_seq', 1, false);


--
-- Name: storage_units_id_seq; Type: SEQUENCE SET; Schema: public; Owner: default
--

SELECT pg_catalog.setval('public.storage_units_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: default
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: storage_grids storage_grids_pkey; Type: CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_grids
    ADD CONSTRAINT storage_grids_pkey PRIMARY KEY (id);


--
-- Name: storage_places storage_places_pkey; Type: CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_places
    ADD CONSTRAINT storage_places_pkey PRIMARY KEY (id);


--
-- Name: storage_units storage_units_pkey; Type: CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_units
    ADD CONSTRAINT storage_units_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: storage_grids storage_grids_storage_place_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_grids
    ADD CONSTRAINT storage_grids_storage_place_id_fkey FOREIGN KEY (storage_place_id) REFERENCES public.storage_places(id);


--
-- Name: storage_units storage_units_storage_grid_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_units
    ADD CONSTRAINT storage_units_storage_grid_id_fkey FOREIGN KEY (storage_grid_id) REFERENCES public.storage_grids(id);


--
-- Name: storage_units storage_units_storage_place_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: default
--

ALTER TABLE ONLY public.storage_units
    ADD CONSTRAINT storage_units_storage_place_id_fkey FOREIGN KEY (storage_place_id) REFERENCES public.storage_places(id);


--
-- PostgreSQL database dump complete
--

